from multiprocessing import Event
from django.shortcuts import render
from . models import news, Event
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
class NewsViewList(ListView):
    model = news
    template_name = "news1/news_list.html"
    context_object_name = "news_list"

class NewsCreateList(CreateView):
    model = news
    fiels = '__all__'
    template_name = "news1/news_create.html"
    success_url = "/news/newslist"

class NewsDetailView(DetailView):
    model = news
    template_name = "news1/news_detail.html"
    context_object_name = "news_detail"

class NewsDeleteView(DeleteView):
    model = news
    template_name = "news1/news_delete.html"
    success_url = "/news/newslist"

class EventCreateView(CreateView):
    model = Event
    fields = "__all__"
    template_name = "news1/event.html"
    success_url = "/"
