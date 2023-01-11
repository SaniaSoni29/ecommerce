from random import choices
from django.db import models
from django.forms import CharField, DateField

# Create your models here.
Task_priority = [("Low","Low"),("Medium","Medium"),("High","High")]
class Task(models.Model):
    task_name = models.CharField(max_length=25)
    task_date = models.DateField()
    task_description = models.CharField(max_length = 100)
    task_priority = models.CharField(choices = Task_priority ,max_length = 25)
