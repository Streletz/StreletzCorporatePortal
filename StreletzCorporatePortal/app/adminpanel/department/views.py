from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from app.adminpanel.department.forms import BootstrapDepartmentCreateForm, BootstrapDepartmentDeleteForm
from app.adminpanel.department.forms import BootstrapDepartmentEditForm

APP_NAME = 'Streletz Кoрпоративный Портал'
VERSION = '0.1.0'


class DepartmentListView(ListView):
    title = 'Подразделения'
    model = Department
    template_name = 'adminpanel/departments/index.html'
    context_object_name = 'departments'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        ctx = super(DepartmentListView, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['app_name'] = APP_NAME
        ctx['version'] = VERSION
        ctx['year'] = datetime.now().year
        return ctx


def departmentCreate(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapDepartmentCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/adminpanel/department')
    else:
        form = BootstrapDepartmentCreateForm()

    return render(request,
                  'adminpanel/departments/create.html',
                  {
                      'title': 'Новое подразделение',
                      'year': datetime.now().year,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })


def departmentEdit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapDepartmentEditForm(request.POST)
        if form.is_valid:
            department = Department.objects.get(pk=id)
            department.name = form.data.get('name')
            department.description = form.data.get('description')
            department.save()
            return HttpResponseRedirect('/adminpanel/department')
    else:
        department = Department.objects.get(pk=id)
        form = BootstrapDepartmentEditForm(instance=department)

    return render(request,
                  'adminpanel/departments/edit.html',
                  {
                      'department': department,
                      'title': 'Редактирование подразделения',
                      'year': datetime.now().year,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })


def departmentDelete(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapDepartmentDeleteForm(request.POST)
        if form.is_valid:
            department = Department.objects.get(pk=id)
            department.delete()
            return HttpResponseRedirect('/adminpanel/department')
    else:
        department = Department.objects.get(pk=id)
        form = BootstrapDepartmentDeleteForm(instance=department)

    return render(request,
                  'adminpanel/departments/delete.html',
                  {
                      'department': department,
                      'title': 'Удаление подразделения',
                      'year': datetime.now().year,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })
