from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import generic
from .models import Film, Category, Country, Director
from django.views.generic.edit import CreateView
from forms  import FilmForm, DirectorForm,ReviewForm
from .models import Film, Director,Review



# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film_form.html'

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director_form.html'

class ReviewCreateView(generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('home')

def home(request):
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'homepage.html', context)

 
def homepage(request):
   
    films = Film.objects.all()

    # Render the homepage 
    return render(request, 'homepage.html', {'films': films})