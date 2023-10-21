from django.shortcuts import render, get_object_or_404
from .models import Book, BookReview
from django.contrib.auth.decorators import login_required

# Create your views here.
def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'books': books})

def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.reviews.all()
    num_reviews = reviews.count()
    avg_rating = book.average_rating()
    return render(request, 'book_details.html', {'book': book, 'reviews': reviews, 'num_reviews': num_reviews, 'avg_rating': avg_rating})

@login_required
def write_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        user = request.user
        review = BookReview.objects.create(book=book, user=user, rating=rating, review_text=review_text)
        review.save()
    return render(request, 'write_review.html', {'book': book})