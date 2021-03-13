"""
Definition of urls for StreletzCorporatePortal.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.adminpanel import admin_panel_views


urlpatterns = [path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view(template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
                 'app_name':views.APP_NAME,
                 'version':views.VERSION
             }),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('adminpanel/', admin_panel_views.adminpanelMain, name='adminpanel'),
    path('adminpanel/departments', admin_panel_views.departmentList.as_view(),name='departments'),
    path('adminpanel/departments/create', admin_panel_views.departmentCreate, name = 'create_department'),
    path('adminpanel/departments/edit/<int:id>', admin_panel_views.departmentEdit, name = 'edit_department')]