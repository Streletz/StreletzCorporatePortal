"""
Definition of models.
"""

from django.db import models
import datetime

class Director(models.Model):    
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

class Department(models.Model):    
    name = models.CharField(max_length=255)

class Employee(models.Model):   
   name = models.CharField(max_length=255)
   created = models.DateTimeField(default=datetime.datetime().now())
   worksSince = models.DateTimeField()
   dismissed = models.DateTimeField()
   isActive = models.BooleanField(default=true)
   department = models.ForeignKey(Department, on_delete=models.PROTECT)

# Create your models here.
