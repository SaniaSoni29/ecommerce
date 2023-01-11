from django import views
from . import views
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('payment/',views.payment)
]
