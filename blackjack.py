from classes.game import BlackjackGame
from database.db_handler import initialize_database
from utils.settings import configure_game

def main():
    print("Welcome to Blackjack!")
    initialize_database()  # Initialize the database
    
    # Configurable settings
    dealer_threshold, num_decks = configure_game()
    
    # Player input for game setup
    num_players = int(input("Enter the number of players: "))
    player_names = [input(f"Enter Player {i+1} name: ") for i in range(num_players)]
    
    # Start game
    game = BlackjackGame(player_names, dealer_threshold, num_decks)
    game.play_game()

if __name__ == "__main__":
    main()
