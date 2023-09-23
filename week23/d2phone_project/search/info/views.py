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
    
def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        person = Person(name=name, phone_number=phone_number)
        person.save()
        return render(request, 'add_person.html')
    else:
        return render(request, 'add_person.html')