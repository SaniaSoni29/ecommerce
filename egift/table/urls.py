from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
   path('index/',views.index),
   path('index1/',views.index1) 
]