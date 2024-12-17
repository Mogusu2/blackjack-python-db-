from database.db_handler import fetch_game_history
from rich.console import Console
from rich.table import Table

def display_game_history():
    console = Console()
    history = fetch_game_history(limit=10)

    if not history:
        console.print("[bold yellow]No game history found.[/bold yellow]")
        return

    # Create the table
    table = Table(title="Game History", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Player Name", style="magenta", justify="center")  # New column
    table.add_column("Player Score", style="green", justify="center")
    table.add_column("Dealer Score", style="red", justify="center")
    table.add_column("Result", style="blue", justify="center")
    table.add_column("Timestamp", style="yellow", justify="center")

    # Add rows to the table
    for record in history:
        table.add_row(
            str(record.id),
            record.player_name,  # Include player name
            str(record.player_score),
            str(record.dealer_score),
            record.result,
            str(record.timestamp)
        )

    console.print(table)

if __name__ == "__main__":
    display_game_history()
