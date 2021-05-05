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


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
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
            'title': 'About',
            'message': 'Your application description page.',
            'year': YEAR,
            'app_name': APP_NAME,
            'version': VERSION
        }
    )
