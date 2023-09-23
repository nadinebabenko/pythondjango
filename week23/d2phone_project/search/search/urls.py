"""
URL configuration for search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from  info  import views

urlpatterns = [
    path('person/<str:number>/', views.display_person_by_phonenumber, name='personbyphone'),
    path('persons/<str:name>/', views.display_person_by_name, name='personsbyname'),
    path('persons/', views.display_all_persons, name='allpersons'),
    path('addperson/', views.add_person, name='addperson'),
]
 