from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Gif, Category

admin.site.register(Gif)
admin.site.register(Category)