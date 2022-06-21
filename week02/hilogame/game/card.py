import random


class Card:

    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 13)
