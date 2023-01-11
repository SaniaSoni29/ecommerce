from django.db import models
from django.forms import CharField, IntegerField
from django.db import models

# Create your models here.
class cart(models.Model):
    cart_id = models.IntegerField()
    cart_name = models.CharField(max_length = 25)
    cart_details = models.TextField(null=True)

    class meta:
        db_table = "Cart" 

class saleswoman(models.Model):
    name = models.CharField(max_length = 25) 
    city = models.TextField()    

    class meta:
        db_table = "saleswoman"

class course(models.Model):
    course_name = models.CharField(max_length = 25)
    course_duration = models.IntegerField()
    course_fees = models.IntegerField()

    class meta:
        db_table = "course"

class student(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE)   
    student_name = models.CharField(max_length = 25)
    student_age = models.IntegerField()
    student_email = models.CharField(max_length = 25)

    class meta:
        db_table = "student" 