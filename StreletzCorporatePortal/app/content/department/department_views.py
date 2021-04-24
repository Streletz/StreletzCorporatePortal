from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView



def departmentView(request, id):
    assert isinstance(request, HttpRequest)
    department = Department.objects.get(pk=id)
    director = None
    if department.director_set.filter(employee__isActive=True).count() > 0:
        director = department.director_set.filter(employee__isActive=True).first().employee
    employees = department.employee_set.filter(isActive=True).all().order_by('name')
    return render(request,
                  'content/departments/view.html',
                  {
                      'department': department,
                      'title': department.name,
                      'app_name': settings.APP_NAME,
                      'version': settings.APP_VERSION,
                      'director': director,
                      'employees': employees
                  })
