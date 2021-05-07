from django.views.generic.list import ListView

from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import render

from app.models import Post

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION
YEAR = settings.APP_YEAR


class PostListView(ListView):
    title = 'Новости'
    model = Post
    template_name = 'content/post/index.html'
    context_object_name = 'posts'
    ordering = ['-created']
    paginate_by = settings.APP_CONTENT_PAGINATE_BY

    def get_context_data(self, **kwargs):
        ctx = super(PostListView, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['app_name'] = APP_NAME
        ctx['version'] = VERSION
        ctx['year'] = YEAR
        return ctx


def postView(request, id):
    assert isinstance(request, HttpRequest)
    post = Post.objects.get(pk=id)
    return render(request,
                  'content/post/view.html',
                  {
                      'post': post,
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'title': post.theme
                  })
