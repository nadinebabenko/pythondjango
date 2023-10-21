from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import   models, Avg
from .models import BookReview, Book

@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    avg_rating = book.reviews.aggregate(Avg('rating'))['rating__avg']
    book.avg_rating = avg_rating
    book.save()