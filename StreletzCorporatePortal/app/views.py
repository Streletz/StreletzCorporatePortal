"""
Definition of views.
"""

from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest

APP_NAME = settings.APP_NAME
VERSION = settings.APP_VERSION
YEAR = settings.APP_YEAR


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': YEAR,
            'app_name': APP_NAME,
            'version': VERSION
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'О Программе',
            'message': 'Your application description page.',
            'year': YEAR,
            'author': settings.APP_AUTHOR_NAME,
            'author_site': settings.APP_AUTHOR_SITE,
            'app_name': APP_NAME,
            'version': VERSION
        }
    )
