from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'category']