"""
Definition of models.
"""
from django.conf import settings
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    description = models.TextField(null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    birthday = models.DateTimeField(null=True)
    worksSince = models.DateTimeField()
    dismissed = models.DateTimeField(null=True)
    isActive = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)

    class Meta:
        unique_together = (('name', 'birthday', 'department', 'position'),)


class Director(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    class Meta:
        unique_together = (('department', 'employee'),)


class Post(models.Model):
    created = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    theme = models.CharField(max_length=255)
    content = models.TextField(null=True)

# Create your models here.
