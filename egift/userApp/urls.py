from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('create/',views.BaseRegisterView.as_view(),name='create'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(template_name ="userApp/login.html"),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('sendmail/',views.sendMail,name='sendMail'),
]