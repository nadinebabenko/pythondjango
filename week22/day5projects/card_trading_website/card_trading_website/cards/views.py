from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def display_all_cards(request):
    cards = Card.objects.filter(current_owner=None)
    return render(request, 'cards/all_cards.html', {'cards': cards})

@login_required
def display_one_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/one_card.html', {'card': card})

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'cards/user_profile.html', {'user_profile': user_profile})

@login_required
def buy_one_card(request, card_id, user_id):
    card = get_object_or_404(Card, pk=card_id)
    user = get_object_or_404(User, pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    if user_profile.money >= card.price:
        card.current_owner = user
        card.save()
        user_profile.money -= card.price
        user_profile.xp_points += card.xp_points
        user_profile.save()
        return redirect('user_profile', user_id=user.id)
    else:
        return render(request, 'cards/error.html', {'error_message': 'You do not have enough money to buy this card.'})

@login_required
def sell_one_card(request, card_id, user_id):
    card = get_object_or_404(Card, pk=card_id)
    user = get_object_or_404(User, pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    if card.current_owner == user:
        card.current_owner = None
        card.previous_owner = user
        card.save()
        user_profile.money += card.price
        user_profile.xp_points -= card.xp_points
        user_profile.save()
        return redirect('user_profile', user_id=user.id)
    else:
        return render(request, 'cards/error.html', {'error_message': 'You do not own this card.'})

# Create your views here.
