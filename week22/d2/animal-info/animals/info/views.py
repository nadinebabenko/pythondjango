from django.shortcuts import render
from .data import animals, families
from templates import *
from django.http import HttpResponse

# Create your views here.
def display_all_animals(request):
    animal_list = []
    for animal in animals:
        animal_info = {
            'name': animal['name'],
            'legs': animal['legs'],
            'weight': animal['weight'],
            'height': animal['height'],
            'speed': animal['speed']
        }
        animal_list.append(animal_info)
    context = {'animal_list': animal_list}
    return render(request, 'all_animals.html', context)

def display_all_families(request):
    family_list = []
    for family in families:
        family_list.append(family['name'])
    context = {'family_list': family_list}
    return render(request, 'all_families.html', context)

def display_one_animal(request, animal_id):
    animal = None
    for a in animals:
        if a['id'] == animal_id:
            animal = a
            break
    if animal is None:
        return HttpResponse('Animal not found')
    context = {'animal': animal}
    return render(request, 'one_animal.html', context)

def display_animal_per_family(request, family_id):
    animal_list = []
    for animal in animals:
        if animal['family'] == family_id:
            animal_info = {
                'name': animal['name'],
                'legs': animal['legs'],
                'weight': animal['weight'],
                'height': animal['height'],
                'speed': animal['speed']
            }
            animal_list.append(animal_info)
    context = {'animal_list': animal_list}
    return render(request, 'animals_per_family.html', context)