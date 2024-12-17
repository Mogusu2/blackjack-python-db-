from classes.deck import Deck
from classes.player import Player
from database.db_handler import save_game_result
from utils.display import display_hand
from rich.console import Console

console = Console()

class BlackjackGame:
    def __init__(self, player_names, dealer_threshold=17, num_decks=1):
        self.deck = Deck(num_decks)
        self.players = [Player(name) for name in player_names]
        self.dealer = Player("Dealer")
        self.dealer_threshold = dealer_threshold

    def play_game(self):
        console.clear()
        print("\nDealing initial cards...")

        # Deal two cards to each player and dealer
        for player in self.players + [self.dealer]:
            player.add_card(self.deck.deal_card())
            player.add_card(self.deck.deal_card())

        # Show initial hands
        for player in self.players:
            console.clear()
            display_hand(player)  # Show player's hand
            display_hand(self.dealer, title="Dealer's Visible Hand")
        
        # Player's turn
        for player in self.players:
            while not player.is_busted():
                console.clear()
                display_hand(player)
                display_hand(self.dealer, title="Dealer's Visible Hand")

                action = input(f"{player.name}, do you want to [H]it or [S]tay? ").upper()
                if action == "H":
                    player.add_card(self.deck.deal_card())
                else:
                    break

                if player.is_busted():
                    console.clear()
                    display_hand(player)
                    print(f"\n{player.name} busted!")

        # Dealer's turn
        console.clear()
        print("\nDealer's turn...")
        while self.dealer.score < self.dealer_threshold:
            self.dealer.add_card(self.deck.deal_card())
            console.clear()
            display_hand(self.dealer, title="Dealer's Hand")

        # Results
        for player in self.players:
            if player.is_busted():
                result = "Loss"
            elif self.dealer.is_busted() or player.score > self.dealer.score:
                result = "Win"
            elif player.score == self.dealer.score:
                result = "Draw"
            else:
                result = "Loss"

            console.clear()
            display_hand(player)
            display_hand(self.dealer, title="Dealer's Hand")
            console.print(f"[bold green]{player.name}: {result}![/bold green]\n")

            save_game_result(player.name, player.score, self.dealer.score, result)
