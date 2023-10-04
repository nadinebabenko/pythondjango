from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm, LoginForm
from django.views import View
from django.contrib import messages
from django.db.models import Max
from .models import Word, HighScore
import random


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('home')



class CountdownGameView(LoginRequiredMixin, View):
    def get(self, request):
        word = Word.objects.filter(length__gte=6).order_by('?').first()
        shuffled_word = ''.join(random.sample(word.word, len(word.word)))
        request.session['shuffled_word'] = shuffled_word
        return render(request, 'countdown.html', {'shuffled_word': shuffled_word})

    def post(self, request):
        shuffled_word = request.session.get('shuffled_word')
        guess = request.POST.get('guess')
        word = Word.objects.filter(word__icontains=guess).first()
        if not word:
            messages.error(request, 'Invalid guess')
            return redirect('countdown')
        if guess == word.word:
            score = 10
        elif len(guess) == len(word.word) - 1:
            score = 5
        elif len(guess) == len(word.word) - 2:
            score = 3
        elif guess == word.word:
            score = 8
        else:
            score = 0
        HighScore.objects.create(user=request.user, word=word, score=score)
        total_score = HighScore.objects.filter(user=request.user).aggregate(Max('score'))['score__max']
        if total_score is None:
            total_score = 0
        if len(request.session.get('guesses', [])) >= 2:
            word = Word.objects.filter(length__gte=6).order_by('?').first()
            shuffled_word = ''.join(random.sample(word.word, len(word.word)))
            request.session['shuffled_word'] = shuffled_word
            request.session['guesses'] = []
        else:
            request.session.setdefault('guesses', []).append(guess)
        return render(request, 'countdown.html', {'word': word.word, 'score': score, 'total_score': total_score, 'shuffled_word': shuffled_word})