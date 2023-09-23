from  django.urls import path
from . import views

urlpatterns = [
    path('add_todo/', views.add_todo, name='add_todo'),
]