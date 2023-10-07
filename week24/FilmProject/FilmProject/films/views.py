from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import ProducerFormSet
from django.views import generic
from .models import Film, Category, Country, Director, CustomUser
from django.views.generic.edit import CreateView
from forms  import FilmForm, DirectorForm,ReviewForm
from .models import Film, Director,Review
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ProducerFormSet(self.request.POST)
        else:
            data['formset'] = ProducerFormSet()
        return data

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = ProducerFormSet(self.request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

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

class FilmDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Film
    success_url = reverse_lazy('films:homepage')
    template_name = 'film_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
def delete_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'POST':
        film.delete()
        messages.success(request, f'{film.title} has been deleted successfully.')
        return redirect('films_list')
    context = {'film': film}
    return render(request, 'confirm_delete.html', context)

class FavouriteFilmView(LoginRequiredMixin, generic.View):
    def post(self, request, *args, **kwargs):
        film_id = request.POST.get('film_id')
        user = request.user
        film = get_object_or_404(Film, id=film_id)
        user.favorite_films.add(film)
        return JsonResponse({'success': True})

    def delete(self, request, *args, **kwargs):
        film_id = request.POST.get('film_id')
        user = request.user
        film = get_object_or_404(Film, id=film_id)
        user.favorite_films.remove(film)
        return JsonResponse({'success': True})
    
class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'film_detail.html'