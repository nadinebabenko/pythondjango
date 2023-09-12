import requests
import json
import random
from cards.models import Card, User



API_URL = 'https://www.potterapi.com/v1/cards'
DB_PATH = 'harry_potter_cards/db.mysql'

def fetch_data():
    response = requests.get('https://hp-api.onrender.com/api/characters')
    return json.loads(response.text)

def parse_data(data):
    cards = []
    for card_data in data:
        card = {
            'name': card_data['name'],
            'type': card_data['type'],
            'rarity': card_data['rarity'],
            'image_url': card_data['image_url'],
            'card_id': card_data['_id'],
            'xp': random.randint(1, 10),
            'price': random.randint(200, 2000),
            'current_owner': None,
            'previous_owner': None,
        }
        cards.append(card)
    return cards

def populate_cards(cards):
    for card in cards:
        Card.objects.create(
            name=card['name'],
            type=card['type'],
            rarity=card['rarity'],
            image_url=card['image_url'],
            card_id=card['card_id'],
            xp=card['xp'],
            price=card['price'],
            current_owner=card['current_owner'],
            previous_owner=card['previous_owner'],
        )

def create_user():
    user = User.objects.create(balance=1000)
    return user

data = fetch_data()
cards = parse_data(data)
populate_cards(cards)
user = create_user()