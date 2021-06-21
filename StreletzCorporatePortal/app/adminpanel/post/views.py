from datetime import datetime

from django.conf import settings
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView

from app.adminpanel.post.forms import BootstrapPostCreateForm, BootstrapPostEditForm, BootstrapPostDeleteForm
from app.models import Post

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION
YEAR = settings.APP_YEAR

class PostListView(ListView):
    title = 'Новости'
    model = Post
    template_name = 'adminpanel/post/index.html'
    context_object_name = 'posts'
    ordering = ['created']
    paginate_by = settings.APP_ADMINPANEL_PAGINATE_BY

    def get_context_data(self, **kwargs):
        ctx = super(PostListView, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['app_name'] = APP_NAME
        ctx['version'] = VERSION
        ctx['year'] = YEAR
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
                      'year': YEAR,
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
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })


def postDelete(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapPostDeleteForm(request.POST)
        if form.is_valid:
            post = Post.objects.get(pk=id)
            post.delete()
            return HttpResponseRedirect('/adminpanel/post')
    else:
        post = Post.objects.get(pk=id)
        form = BootstrapPostDeleteForm(instance=post)


    return render(request,
                  'adminpanel/post/delete.html',
                  {
                      'post': post,
                      'title': 'Удаление новости',
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })
