from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    todos = Todo.objects.all()
    context = {'form': form, 'todos': todos}
    return render(request, 'todos/todo_list.html', context)

 
