import random
from classes.card import Card

class Deck:
    def __init__(self, num_decks=1):
        self.cards = []
        suits = ["♠", "♥", "♦", "♣"]
        ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
                 "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

        for _ in range(num_decks):
            for suit in suits:
                for rank, value in ranks.items():
                    self.cards.append(Card(rank, suit, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
