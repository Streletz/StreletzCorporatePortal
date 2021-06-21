from django import template  # нужен для регистрации шаблонного тега
from django.conf import settings

from app.models import Post

register = template.Library()  # тут мы присваем значение


@register.inclusion_tag(
    '../templates/app/ui_modules/last_posts.html')
def last_posts():
    posts = Post.objects.all().order_by('-created')[:settings.APP_LAST_POSTS_COUNT]
    return {'posts': posts}
