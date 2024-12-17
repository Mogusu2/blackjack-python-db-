from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection
DATABASE_URL = "sqlite:///database/blackjack_results.db"
engine = create_engine(DATABASE_URL, echo=True)  # Debug SQL queries
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Game results table
class GameResult(Base):
    __tablename__ = "game_results"

    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)  # Player name column
    player_score = Column(Integer, nullable=False)
    dealer_score = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())

# Initialize the database
def init_db():
    Base.metadata.create_all(engine)

# Save a game result
def save_game_result(player_name, player_score, dealer_score, result):
    session = Session()
    game_result = GameResult(
        player_name=player_name,
        player_score=player_score,
        dealer_score=dealer_score,
        result=result
    )
    session.add(game_result)
    session.commit()
    session.close()

# Fetch game history
def fetch_game_history(limit=10):
    session = Session()
    history = session.query(GameResult).order_by(GameResult.timestamp.desc()).limit(limit).all()
    session.close()
    return history

# Run this to initialize the database
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
