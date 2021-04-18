"""
Definition of urls for StreletzCorporatePortal.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.adminpanel import admin_panel_views
from app.adminpanel.department import views as admin_department_views
from app.adminpanel.position import views as admin_position_views

from app.content.department import department_views
from app.content.employee import employee_views

urlpatterns = [path('', views.home, name='home'),
               path('contact/', views.contact, name='contact'),
               path('about/', views.about, name='about'),
               path('login/',
                    LoginView.as_view(template_name='app/login.html',
                                      authentication_form=forms.BootstrapAuthenticationForm,
                                      extra_context=
                                      {
                                          'title': 'Log in',
                                          'year': datetime.now().year,
                                          'app_name': views.APP_NAME,
                                          'version': views.VERSION
                                      }),
                    name='login'),
               path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
               path('admin/', admin.site.urls),
               # ADMIN PANEL
               path('adminpanel/', admin_panel_views.adminpanelMain, name='adminpanel'),
               path('adminpanel/department', admin_department_views.DepartmentListView.as_view(), name='departments'),
               path('adminpanel/department/create', admin_department_views.departmentCreate, name='create_department'),
               path('adminpanel/department/edit/<int:id>', admin_department_views.departmentEdit,
                    name='edit_department'),
               path('adminpanel/department/delete/<int:id>', admin_department_views.departmentDelete,
                    name='delete_department'),
               path('adminpanel/position', admin_position_views.PositionListView.as_view(), name='positions'),
               path('adminpanel/position/create', admin_position_views.positionCreate, name='create_position'),
               path('adminpanel/position/edit/<int:id>', admin_position_views.positionEdit,
                    name='edit_position'),
               path('adminpanel/position/delete/<int:id>', admin_position_views.positionDelete,
                    name='delete_position'),
               # PUBLIC SITE
               path('department/<int:id>', department_views.departmentView, name='department_content_view'),
               path('employee/<int:id>', employee_views.employeeCardView, name='employee_content_view')
               ]
