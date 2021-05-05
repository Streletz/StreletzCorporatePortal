from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import render

from app.models import Department

YEAR = settings.APP_YEAR

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
                      'year':YEAR,
                      'app_name': settings.APP_NAME,
                      'version': settings.APP_VERSION,
                      'director': director,
                      'employees': employees
                  })
