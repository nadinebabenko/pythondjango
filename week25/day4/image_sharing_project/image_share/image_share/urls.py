"""
URL configuration for image_share project.

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
from imageshare.views import SignUpView, MyLoginView, ImageListView, MyImageView, ImageCreateView

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('my-images/', MyImageView.as_view(), name='my_image_list'),
    path('upload/', ImageCreateView.as_view(), name='image_upload'),
     
]
