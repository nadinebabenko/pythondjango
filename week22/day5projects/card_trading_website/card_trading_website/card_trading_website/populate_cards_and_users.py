import random
from faker import Faker

fake = Faker()

class User:
    def __init__(self, username, email, points=0, amount_of_money=1000):
        self.username = username
        self.email = email
        self.points = points
        self.amount_of_money = amount_of_money
        self.cards = []

    def buy_card(self, card):
        if self.amount_of_money >= card.price:
            self.amount_of_money -= card.price
            self.points += card.points
            self.cards.append(card)
            if card.previous_owner:
                card.previous_owner.amount_of_money += card.price
        else:
            print("Not enough money to buy card")

class Card:
    def __init__(self, price, points, previous_owner=None):
        self.price = price
        self.points = points
        self.previous_owner = previous_owner

def generate_users_and_cards(num_users):
    users = []
    for i in range(num_users):
        username = fake.user_name()
        email = fake.email()
        user = User(username, email)
        num_cards = random.randint(1, 10)
        for j in range(num_cards):
            price = random.randint(1, 100)
            points = random.randint(1, 10)
            card = Card(price, points, user)
            user.buy_card(card)
        users.append(user)
    return users