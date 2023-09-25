import requests
import random
from faker import Faker
from gifts.models import Gif, Category

 
categories = ['Funny', 'Cute', 'Sports', 'Music', 'Animals', 'Food', 'Travel', 'Art', 'Science', 'Nature']

 
response = requests.get('https://api.giphy.com/v1/gifs/trending?limit=20&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
data = response.json()

 
fake = Faker()
for gif_data in data['data']:
    gif = Gif.objects.create(
        title=gif_data['title'],
        url=gif_data['images']['original']['url'],
        uploader_name=fake.name(),
    )
    categories = random.sample(categories, 2)
    for category_name in categories:
        category, _ = Category.objects.get_or_create(name=category_name)
        gif.categories.add(category)