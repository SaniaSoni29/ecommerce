from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
   path('newslist/',views.NewsViewList.as_view(),name = 'news_list'),
   path('createnews/',views.NewsCreateList.as_view(),name = 'news_create'),
   path('newsdetails/<int:pk>/',views.NewsDetailView.as_view(),name = 'news_details'),
   path('newsdelete/<int:pk>/',views.NewsDeleteView.as_view(),name = 'news_delete'),
   path('event/',views.EventCreateView.as_view(),name = 'event_create')
]