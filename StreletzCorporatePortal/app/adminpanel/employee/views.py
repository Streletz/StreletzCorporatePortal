from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department, Employee, Position
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from app.adminpanel.employee.forms import BootstrapEmployeeCreateForm, \
    BootstrapEmployeeEditForm, BootstrapEmployeeDeleteForm

YEAR = settings.APP_YEAR


class EmployeeListView(ListView):
    title = 'Сотрудники'
    model = Employee
    template_name = 'adminpanel/employee/index.html'
    context_object_name = 'employees'
    ordering = ['name']
    paginate_by = settings.APP_ADMINPANEL_PAGINATE_BY

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeListView, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['app_name'] = settings.APP_NAME
        ctx['version'] = settings.APP_VERSION
        ctx['year'] = YEAR
        return ctx


def employeeCreate(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapEmployeeCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/adminpanel/employee')
    else:
        form = BootstrapEmployeeCreateForm()

    return render(request,
                  'adminpanel/employee/create.html',
                  {
                      'title': 'Новый сотрудник',
                      'year': YEAR,
                      'app_name': settings.APP_NAME,
                      'version': settings.APP_VERSION,
                      'form': form
                  })


def employeeEdit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapEmployeeEditForm(request.POST)
        if form.is_valid:
            employee = Employee.objects.get(pk=id)
            employee.name = form.data.get('name')
            employee.birthday = form.data.get('birthday')
            employee.worksSince = form.data.get('worksSince')
            # Обработка увольнения сотрудника
            is_active = form.data.get('isActive') is not None
            employee.isActive = is_active
            if is_active:
                employee.dismissed = None
            else:
                if form.data.get('dismissed') is not None and form.data.get('dismissed') != '':
                    employee.dismissed = form.data.get('dismissed')
                else:
                    employee.dismissed = datetime.now()
            # Выбираем подразделение и должность
            employee.department = Department.objects.get(pk=form.data.get('department'))
            employee.position = Position.objects.get(pk=form.data.get('position'))
            employee.save()
            return HttpResponseRedirect('/adminpanel/employee')
    else:
        employee = Employee.objects.get(pk=id)
        form = BootstrapEmployeeEditForm(instance=employee)

    return render(request,
                  'adminpanel/employee/edit.html',
                  {
                      'employee': employee,
                      'title': 'Редактирование сотрудника',
                      'year': YEAR,
                      'app_name': settings.APP_NAME,
                      'version': settings.APP_VERSION,
                      'form': form
                  })


def employeeDelete(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapEmployeeDeleteForm(request.POST)
        if form.is_valid:
            employee = Employee.objects.get(pk=id)
            employee.delete()
            return HttpResponseRedirect('/adminpanel/employee')
    else:
        employee = Employee.objects.get(pk=id)
        form = BootstrapEmployeeDeleteForm(instance=employee)

    return render(request,
                  'adminpanel/employee/delete.html',
                  {
                      'employee': employee,
                      'title': 'Удаление сотрудника',
                      'year': YEAR,
                      'app_name': settings.APP_NAME,
                      'version': settings.APP_VERSION,
                      'form': form
                  })
