from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Department, Employee, Director, Post
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from app.adminpanel.department.forms import BootstrapDepartmentDeleteForm, BootstrapDepartmentCreateForm
from app.adminpanel.department.forms import BootstrapDepartmentEditForm

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION


class PostListView(ListView):
    title = 'Новости'
    model = Post
    template_name = 'adminpanel/post/index.html'
    context_object_name = 'posts'
    ordering = ['created']

    def get_context_data(self, **kwargs):
        ctx = super(PostListView, self).get_context_data(**kwargs)
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
            director_id = int(form.data.get('director'))
            new_director = Employee.objects.get(pk=director_id)
            if director_id > 0:
                director = None
                if department.director_set.count() > 0:
                    director = department.director_set.filter(employee__isActive=True).first()
                else:
                    director = Director()
                    director.department = department
                director.employee = new_director
                director.save()
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
