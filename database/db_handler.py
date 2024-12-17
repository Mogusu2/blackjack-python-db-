from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import pytz  # For time zone handling

# Database setup
DATABASE_URL = "sqlite:///blackjack.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Game result model
class GameResult(Base):
    __tablename__ = "game_results"

    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)
    player_score = Column(Integer, nullable=False)
    dealer_score = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(pytz.timezone("Africa/Nairobi")))

# Create the table if it does not exist
def initialize_database():
    Base.metadata.create_all(engine)

# Save a game result
def save_game_result(player_name, player_score, dealer_score, result):
    game_result = GameResult(
        player_name=player_name,
        player_score=player_score,
        dealer_score=dealer_score,
        result=result
    )
    session.add(game_result)
    session.commit()
    print(f"Game result saved for {player_name} at {datetime.now(pytz.timezone('Africa/Nairobi'))}")

# Fetch game history
def fetch_game_history(limit=10):
    return session.query(GameResult).order_by(GameResult.timestamp.desc()).limit(limit).all()

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Blackjack Database Handler")
    parser.add_argument("--history", action="store_true", help="Show game history")

    args = parser.parse_args()

    initialize_database()

    if args.history:
        results = fetch_game_history()
        print("\nGame History:")
        for result in results:
            print(f"ID: {result.id} | Player: {result.player_name} | Player Score: {result.player_score} | "
                  f"Dealer Score: {result.dealer_score} | Result: {result.result} | "
                  f"Timestamp: {result.timestamp}")
