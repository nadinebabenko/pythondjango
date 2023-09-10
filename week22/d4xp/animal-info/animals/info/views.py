from django.shortcuts import render
from .models import Animal, Family

# Create your views here.
def display_all_animals(request):
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, 'animals.html', context)

def display_all_families(request):
    families = Family.objects.all()
    context = {'families': families}
    return render(request, 'families.html', context)

def display_one_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    context = {'animal': animal}
    return render(request, 'animal.html', context)

def display_animal_per_family(request, family_id):
    animals = Animal.objects.filter(family__id=family_id)
    context = {'animals': animals}
    return render(request, 'animals.html', context)