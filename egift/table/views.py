from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    course_list = course.objects.all().values_list()
    course_list1 = course.objects.filter(course_name__startswith = 'j').values_list()
    course_list2 = course.objects.filter(course_fees__lt = 40000)
    print(course_list)
    print(course_list1)
    print(course_list2)
    return HttpResponse("heelloooo") 

def index1(request):
    student_details = student.objects.all().values_list()
    student_details1 = student.objects.all().values('course__course_name','student_name','student_age')
    print(student_details)
    print(student_details1)
    return HttpResponse("Hi")
