from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION


def adminpanelMain(request):
    assert isinstance(request, HttpRequest)
    return render(request,
                  'adminpanel/index.html',
                  {
                      'title': 'Панель администратора',
                      'year': datetime.now().year,
                      'app_name': APP_NAME,
                      'version': VERSION
                  })