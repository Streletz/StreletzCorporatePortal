from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

APP_NAME = 'Streletz Кoрпоративный Портал'
VERSION = '0.1.0'


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