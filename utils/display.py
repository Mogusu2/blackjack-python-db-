from rich.console import Console
from rich.table import Table
from rich.padding import Padding
from rich.box import SQUARE  # Import for table box styling
from rich.text import Text

console = Console()

# Function to colorize suits
def colorize_card(card):
    suit_colors = {
        "♥": "red",    # Hearts are red
        "♦": "bright_red",  # Diamonds are bright red
        "♠": "white",  # Spades are white
        "♣": "green",  # Clubs are green
    }
    suit = card.suit
    rank = card.rank
    color = suit_colors.get(suit, "white")  # Default to white if unknown suit
    return Text(f"{rank} of {suit}", style=color)

# Display hand in a single table
def display_hand(player, title=None):
    """
    Display a player's or dealer's hand dynamically in a clean, formatted table.
    Shows all cards with colored suits and totals the hand value.
    """
    table = Table(title=title or f"{player.name}'s Hand", show_header=False, header_style="bold cyan", box=SQUARE)

    table.add_column("Card", justify="center", style="bold white", width=14)

    # Add cards with colored suits
    for card in player.hand:
        table.add_row(colorize_card(card))

    # Calculate and display the total value of the cards
    total_value = sum(card.value for card in player.hand)  # Assuming card has `value` attribute
    table.add_row("─" * 14)  # Add a separator row
    table.add_row(f"[bold yellow]Total: {total_value}[/bold yellow]")

    # Print the table with padding for better formatting
    console.print(Padding(table, (1, 0, 1, 0)))
