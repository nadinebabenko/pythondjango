from django.shortcuts import render
from .models import Todo, Category

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        deadline_date = request.POST.get('deadline_date')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        todo = Todo.objects.create(title=title, details=details, deadline_date=deadline_date, category=category)
        todos = Todo.objects.all()
        return render(request, 'todos.html', {'todos': todos})
    else:
        todos = Todo.objects.all()
        categories = Category.objects.all()
        return render(request, 'add_todo.html', {'todos': todos, 'categories': categories})