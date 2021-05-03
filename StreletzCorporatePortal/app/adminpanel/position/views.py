from datetime import datetime

from django.conf import settings
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from app.adminpanel.position.forms import BootstrapPositionCreateForm, BootstrapPositionEditForm, \
    BootstrapPositionDeleteForm
from app.models import Position

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION
YEAR = datetime.now().year


class PositionListView(ListView):
    title = 'Должности'
    model = Position
    template_name = 'adminpanel/position/index.html'
    context_object_name = 'positions'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        ctx = super(PositionListView, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['app_name'] = APP_NAME
        ctx['version'] = VERSION
        ctx['year'] = YEAR
        return ctx


def positionCreate(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapPositionCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/adminpanel/position')
    else:
        form = BootstrapPositionCreateForm()

    return render(request,
                  'adminpanel/position/create.html',
                  {
                      'title': 'Новая должность',
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })


def positionEdit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapPositionEditForm(request.POST)
        if form.is_valid:
            position = Position.objects.get(pk=id)
            position.name = form.data.get('name')
            position.save()
            return HttpResponseRedirect('/adminpanel/position')
    else:
        position = Position.objects.get(pk=id)
        form = BootstrapPositionEditForm(instance=position)

    return render(request,
                  'adminpanel/position/edit.html',
                  {
                      'position': position,
                      'title': 'Редактирование должности',
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })


def positionDelete(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = BootstrapPositionDeleteForm(request.POST)
        if form.is_valid:
            position = Position.objects.get(pk=id)
            position.delete()
            return HttpResponseRedirect('/adminpanel/position')
    else:
        position = Position.objects.get(pk=id)
        form = BootstrapPositionDeleteForm(instance=position)

    return render(request,
                  'adminpanel/position/delete.html',
                  {
                      'position': position,
                      'title': 'Удаление должности',
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION,
                      'form': form
                  })
