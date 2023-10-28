"""
URL configuration for management project.

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
from django.urls import path
from managements.crud import DepartmentAPIView, EmployeeAPIView, ProjectAPIView, TaskAPIView
 

urlpatterns = [
    path('departments/', DepartmentAPIView.as_view(), name='department-list-create'),
    path('employees/', EmployeeAPIView.as_view(), name='employee-list-create'),
    path('projects/<int:pk>/', ProjectAPIView.as_view(), name='project-retrieve-update-delete'),
    path('tasks/<int:pk>/', TaskAPIView.as_view(), name='task-retrieve-update-delete'),
]