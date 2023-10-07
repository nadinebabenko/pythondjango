from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Image
from .forms import ImageForm



# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class MyLoginView(LoginView):
    template_name = 'login.html'
    pass

class ImageListView(LoginRequiredMixin, generic.ListView):
    model = Image
    template_name = 'image_list.html'
    context_object_name = 'images'

class MyImageView(LoginRequiredMixin, generic.ListView):
    model = Image
    template_name = 'my_image_list.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

class ImageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'image_form.html'
    success_url = reverse_lazy('image_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from imageshare.models import Profile

@login_required
def profile(request):
   
    profile = Profile.objects.get(user=request.user)
    
    profiles = Profile.objects.all()
    
    return render(request, 'profile.html', {'profile': profile, 'profiles': profiles})