from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
   path('index/',views.index),
   path('contactus/',views.contactus), 
   path('aboutus/',views.aboutus),
   path('feedback/',views.feedback)
]