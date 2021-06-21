from django import template  # нужен для регистрации шаблонного тега

from app.models import Department

register = template.Library()  # тут мы присваем значение


@register.inclusion_tag(
    '../templates/app/ui_modules/department_menu.html')
def department_menu():
    departments = Department.objects.all().order_by('name')
    return {'departments': departments}
