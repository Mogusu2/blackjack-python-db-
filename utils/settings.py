def configure_game():
    dealer_threshold = int(input("Set dealer's hit threshold (default 17): ") or 17)
    num_decks = int(input("Number of decks to use (default 1): ") or 1)
    return dealer_threshold, num_decks
