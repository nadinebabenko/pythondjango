from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cards, name='all_cards'),
    path('<int:card_id>/', views.card_detail, name='card_detail'),
    path('buy/<int:card_id>/<int:user_id>/', views.buy_card, name='buy_card'),
    path('sell/<int:card_id>/<int:user_id>/', views.sell_card, name='sell_card'),
    # ...
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
]