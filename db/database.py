from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# sqlite database path
DATABASE_URL = "sqlite:///bot.db"

# create connection engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} #with threads
)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Helper function to use sessions with "with"
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
