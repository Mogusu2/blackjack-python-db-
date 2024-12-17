class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.calculate_score()

    def calculate_score(self):
        self.score = sum(card.value for card in self.hand)
        # Adjust for Aces
        aces = [card for card in self.hand if card.rank == "A"]
        while self.score > 21 and aces:
            self.score -= 10
            aces.pop()

    def is_busted(self):
        return self.score > 21

    def __str__(self):
        return f"{self.name} - Score: {self.score}"
