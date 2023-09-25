from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    username = forms.CharField(max_length=30, required=True, help_text='Required.')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required.')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required.')
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required.')

    class Meta:
        fields = ('username', 'password')
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating', 'review_author']
        widgets = {
            'review_author': forms.HiddenInput()
        }