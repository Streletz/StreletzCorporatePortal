from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department, Employee
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION
YEAR = settings.APP_YEAR


def employeeCardView(request, id):
    assert isinstance(request, HttpRequest)
    employee = Employee.objects.get(pk=id)
    return render(request,
                  'content/employee/view.html',
                  {
                      'employee': employee,
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'title': employee.name
                  })
