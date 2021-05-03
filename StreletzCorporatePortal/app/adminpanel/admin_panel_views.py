from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION
YEAR = datetime.now().year


def adminpanelMain(request):
    assert isinstance(request, HttpRequest)
    return render(request,
                  'adminpanel/index.html',
                  {
                      'title': 'Панель администратора',
                      'year': YEAR,
                      'app_name': APP_NAME,
                      'version': VERSION
                  })