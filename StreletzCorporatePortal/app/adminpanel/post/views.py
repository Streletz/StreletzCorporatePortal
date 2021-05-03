from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest

from app.adminpanel.post.forms import BootstrapPostCreateForm, BootstrapPostEditForm
from app.models import Department, Employee, Director, Post
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from app.adminpanel.department.forms import BootstrapDepartmentDeleteForm
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


def postCreate(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapPostCreateForm(request.POST)
        if form.is_valid:
            post = Post()
            post.theme = form.data.get('theme')
            post.content = form.data.get('content')
            post.created = datetime.now()
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/adminpanel/post')
    else:
        form = BootstrapPostCreateForm()

    return render(request,
                  'adminpanel/post/create.html',
                  {
                      'title': 'Добавление новости',
                      'year': datetime.now().year,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })


def postEdit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapPostEditForm(request.POST)
        if form.is_valid:
            post = Post.objects.get(pk=id)
            post.theme = form.data.get('theme')
            post.content = form.data.get('content')
            post.save()
            return HttpResponseRedirect('/adminpanel/post')
    else:
        post = Post.objects.get(pk=id)
        form = BootstrapPostEditForm(instance=post)

    return render(request,
                  'adminpanel/post/edit.html',
                  {
                      'post': post,
                      'title': 'Редактирование новости',
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
