from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
   path('store/',views.store,name = "store"),
   path('cart/',views.cart,name = "cart"), 
   path('checkout/',views.checkout,name = "checkout"),
   path('update-item/',views.updateItem,name = "update-item")
]

