from django.contrib import admin
from .models import Category, Brand, Gifts

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Gifts)