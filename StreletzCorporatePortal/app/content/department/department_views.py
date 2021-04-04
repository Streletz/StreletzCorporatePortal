from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

VERSION = '0.1.0'

def departmentView(request, id):
    assert isinstance(request, HttpRequest)
    department = Department.objects.get(pk=id)
    return render(request,
              'content/departments/view.html',
              {
                  'department': department,
                  'title': department.name,
                  'version': VERSION
              })
