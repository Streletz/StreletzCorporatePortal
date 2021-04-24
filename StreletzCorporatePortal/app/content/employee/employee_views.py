from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department, Employee
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

VERSION = '0.2.0'

def employeeCardView(request, id):
    assert isinstance(request, HttpRequest)
    employee = Employee.objects.get(pk=id)
    return render(request,
              'content/employee/view.html',
              {
                  'employee': employee,
                  'year': datetime.now().year,
                  'app_name': settings.APP_NAME,
                  'version': settings.APP_VERSION,
                  'title': employee.name
              })
