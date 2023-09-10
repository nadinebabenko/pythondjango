from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def display_person_by_phonenumber(request, number):
    try:
        person = Person.objects.get(phone_number=number)
        return render(request, 'person.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponse("No person found with phone number %s." % number)

def display_person_by_name(request, name):
    persons = Person.objects.filter(name__icontains=name)
    if persons:
        return render(request, 'persons.html', {'persons': persons})
    else:
        return HttpResponse("No person found with name %s." % name)