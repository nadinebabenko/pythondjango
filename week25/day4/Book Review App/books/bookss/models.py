import requests
from django.db import   models, Avg
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=20)
    avg_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

def average_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg']

def get_books_from_api():
    url = 'https://www.googleapis.com/books/v1/volumes?q=python'
    response = requests.get(url)
    data = response.json()
    books = []
    for item in data['items']:
        book = {}
        book['title'] = item['volumeInfo']['title']
        book['author'] = item['volumeInfo']['authors'][0]
        book['published_date'] = item['volumeInfo']['publishedDate']
        book['description'] = item['volumeInfo']['description']
        book['page_count'] = item['volumeInfo']['pageCount']
        if 'categories' in item['volumeInfo']:
            book['categories'] = ', '.join(item['volumeInfo']['categories'])
        else:
            book['categories'] = ''
        book['thumbnail_url'] = item['volumeInfo']['imageLinks']['thumbnail']
        books.append(book)
    return books

def save_books_to_db(books):
    for book in books:
        Book.objects.create(
            title=book['title'],
            author=book['author'],
            published_date=book['published_date'],
            description=book['description'],
            page_count=book['page_count'],
            categories=book['categories'],
            thumbnail_url=book['thumbnail_url']
        )

books = get_books_from_api()
save_books_to_db(books)

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()