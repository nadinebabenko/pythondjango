from django.shortcuts import render


name = 'Bob Smith'
age = 35
country = 'USA'
people = ['bob', 'martha', 'fabio', 'john']

all_people = [
    {
        'id': 1,
        'name': 'Bob Smith',
        'age': 35,
        'country': 'USA'
    },
    {
        'id': 2,
        'name': 'Martha Smith',
        'age': 60,
        'country': 'USA'
    },
    {
        'id': 3,
        'name': 'Fabio Alberto',
        'age': 18,
        'country': 'Italy'
    },
    {
        'id': 4,
        'name': 'Dietrich Stein',
        'age': 85,
        'country': 'Germany'
    }
]

# Create your views here.
def display_person(request):
    context = {
        'name': name,
        'age': age,
        'country': country
    }

    return render(request, 'person.html', context)


def display_people(request):
    sorted_people = sorted([name.capitalize() for name in people])
    print(sorted_people)
    context = {
        'sorted_people': sorted_people
    }

    return render(request, 'people.html', context)


def display_all_people(request):
    sorted_age_people = sorted(all_people, key=lambda x: x['age'])
    print(sorted_age_people)
    context = {
        'sorted_age_people': sorted_age_people
    }
    return render(request, 'all_people.html', context)