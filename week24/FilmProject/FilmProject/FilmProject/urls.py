"""
URL configuration for FilmProject project.

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
from . import views
from  films.views import HomePageView, FilmCreateView, DirectorCreateView, ReviewCreateView, FilmDeleteView, FavouriteFilmView, FilmDetailView
 


urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('addFilm/', FilmCreateView.as_view(), name='addFilm'),
    path('addDirector/', DirectorCreateView.as_view(), name='addDirector'),
    path('addReview/', ReviewCreateView.as_view(), name='add_review'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),     
    path('film/<int:pk>/delete/', FilmDeleteView.as_view(), name='delete_film'),
    path('films/<int:film_id>/favorite/', FavouriteFilmView.as_view(), name='favorite_film'),
     path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('films/<int:film_id>/favorite/', FavouriteFilmView.as_view(), name='favorite_film'),
]
]

 
 