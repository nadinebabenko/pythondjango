from django.db import models
from django.utils import timezone
from .models import Film

class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'films'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        app_label = 'films'

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        app_label = 'films'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Film(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    reviews = models.ManyToManyField('Review', related_name='films')

    def __str__(self):
        return self.title

class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    
