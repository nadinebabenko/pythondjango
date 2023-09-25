from django.shortcuts import render
from .models import Gif
from forms import GifSearchForm
 
 

def homepage(request):
    form = GifSearchForm(request.GET)
    gifs = Gif.objects.all()

    if form.is_valid() and form.cleaned_data['search_query']:
        search_query = form.cleaned_data['search_query']
        gifs = gifs.filter(models.Q(title__icontains=search_query) | models.Q(categories__name__icontains=search_query))

    return render(request, 'homepage.html', {'gifs': gifs, 'form': form})

def gif_view(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    if request.method == 'POST':
        if 'increment_likes' in request.POST:
            gif.likes += 1
            gif.save()
        elif 'decrement_likes' in request.POST:
            gif.likes -= 1
            gif.save()
    return render(request, 'gif_view.html', {'gif': gif})

def positive_likes(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    return render(request, 'positive_likes.html', {'gifs': gifs})