from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("heelloooo")


def contactus(request):
    return HttpResponse("Contact Details: +91 0123456789")


def feedback(request):
    return HttpResponse("This is feedback!!")


def aboutus(request):
    return HttpResponse("We are awesome!!")