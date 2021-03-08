"""
Definition of models.
"""

from django.db import models
import datetime
class Department(models.Model):    
    name = models.CharField(max_length=255)

class Position(models.Model):    
    name = models.CharField(max_length=255)

class Employee(models.Model):   
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.datetime.now())
    birthday = models.DateTimeField()
    worksSince = models.DateTimeField()
    dismissed = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)

class Director(models.Model):    
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)



# Create your models here.
