import requests
import random
from django.core.management.base import BaseCommand
from datetime import datetime
from cards.models import Card


class Command(BaseCommand):
    help = 'Populates the Card model with data from the Harry Potter API'

    def handle(self, *args, **kwargs):
        # Harry Potter API endpoint
        api_url = "https://hp-api.onrender.com/api/characters"

        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Failed to fetch data from Harry Potter API'))
            return

        characters = response.json()

        # Clear existing cards
        Card.objects.all().delete()

        # Populate the Card model with the retrieved card information
        for character in characters:
            name_character = character['name']
            species = character.get('species', '')
            house = character.get('house', '')
            image_url = character.get('image', '')
            date_of_birth = character.get('dateOfBirth', '')
            patronus = character.get('patronus', '')
            price = random.randint(200, 2000)
            xp_points = random.randint(1, 10)
            current_owner = None
            previous_owner = None

            if date_of_birth:
                date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").strftime("%Y-%m-%d")

            card = Card(
                name_character=name_character,
                species=species,
                house=house,
                image_url=image_url,
                date_of_birth=date_of_birth,
                patronus=patronus,
                price=price,
                xp_points=xp_points,
                current_owner=current_owner,
                previous_owner=previous_owner
            )

            card.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated cards from the Harry Potter API'))