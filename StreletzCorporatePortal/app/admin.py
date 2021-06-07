from django.contrib import admin

from app.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_filter = ["name"]