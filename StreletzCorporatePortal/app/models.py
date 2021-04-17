"""
Definition of models.
"""

from django.db import models
import datetime
class Department(models.Model):    
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True)

class Position(models.Model):    
    name = models.CharField(max_length=255,unique=True)

class Employee(models.Model):   
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.datetime.now())
    birthday = models.DateTimeField(null=True)
    worksSince = models.DateTimeField(default=datetime.datetime.now())
    dismissed = models.DateTimeField(null=True)
    isActive = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    class Meta:
        unique_together= (('name', 'birthday','department','position'),)

class Director(models.Model):    
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)



# Create your models here.
