from django.shortcuts import render
from .populate_gifs import fetch_gifs
from .forms import GifSearchForm
from .models import Gif, Category

# Create your views here.
def homepage(request):
    form = GifSearchForm(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data.get('search_term')
        gifs = fetch_gifs(search_term)
    else:
        gifs = fetch_gifs()
    return render(request, 'homepage.html', {'gifs': gifs, 'form': form})

def popular_gifs(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    return render(request, 'popular_gifs.html', {'gifs': gifs})