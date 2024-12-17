# Blackjack Python Game with Database Integration

## Overview  
This is a **terminal-based Blackjack game** built in Python with SQLite database integration. The project allows players to play the game, save results (including player name, scores, and outcome), and view their game history in a beautiful **rich table format**.

---

## Features  
- 🎮 **Interactive Gameplay**: Play Blackjack in the terminal with automated dealer scoring.  
- 🧩 **Database Integration**: Results are saved in an SQLite database, including player name, scores, result, and timestamp.  
- 📊 **Game History Table**: Display past game results using a rich table view.  
- 💾 **Persistent Storage**: Game results persist even after the program restarts.

---

## Setup Instructions  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.8 or higher  
- Virtual Environment (optional but recommended)  

### Installation  

1. **Clone the repository**:
   ```bash
   git clone <repo-link>
   cd blackjack-py-db
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:  
   Create the required SQLite database tables.  
   ```bash
   python database/db_handler.py
   ```

---

## How to Run  

### 1. Play the Game  
Run the main game file and follow the prompts:  
```bash
python main_game.py
```

- Enter your name.  
- View your score and the dealer's score.  
- Results are saved automatically to the database.

### 2. View Game History  
Run the following to display past game results in a table:  
```bash
python view_history.py
```

---

## Sample Outputs  

### Gameplay Example  
```
Enter your name: Jamie  
Welcome, Jamie!

Your Score: 21  
Dealer's Score: 18  
Result: Win  
Game result saved!
```

### Game History Table  
```
┌────┬───────────────┬───────────────┬───────────────┬────────┬────────────────────┐
│ ID │ Player Name   │ Player Score  │ Dealer Score  │ Result │ Timestamp          │
├────┼───────────────┼───────────────┼───────────────┼────────┼────────────────────┤
│  1 │ Jamie         │  21           │  18           │ Win    │ 2024-12-17 15:23   │
│  2 │ Sarah         │  19           │  20           │ Loss   │ 2024-12-17 15:25   │
└────┴───────────────┴───────────────┴───────────────┴────────┴────────────────────┘
```

---

## Dependencies  
This project uses the following libraries:
- **SQLAlchemy**: ORM for database interactions.  
- **Rich**: Beautiful terminal table and text formatting.

Install all dependencies using:  
```bash
pip install -r requirements.txt
```

---

## Future Improvements  
- Add multiple rounds of gameplay in a single session.  
- Implement dealer logic for more realistic play.  
- Create a user interface (GUI) using libraries like Tkinter or PyQt.  

---

## Contributing  
Pull requests are welcome! For significant changes, please open an issue first to discuss the proposed changes.  

---

---

## Author  
**Jamie**  
- GitHub: [Mogusu2](https://github.com/Mogusu2)  
- LinkedIn: [James Maroko](https://www.linkedin.com/in/james-maroko/)

---