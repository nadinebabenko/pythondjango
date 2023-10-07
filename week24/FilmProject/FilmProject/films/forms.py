from django import forms
from django.forms import formset_factory
from .models import Film, Director, Review, Producer

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_date', 'created_in_country', 'available_in_countries', 'category', 'director']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'nationality']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['film', 'director', 'rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'rating'}),
        }

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['first_name', 'last_name', 'nationality']

ProducerFormSet = formset_factory(ProducerForm, extra=1)

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'addFilm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = ProducerFormSet()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = ProducerFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )