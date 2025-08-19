import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()  # read .env in the root of the project

# URL of .env 
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://botuser:botpass@localhost:5432/botdb"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,       
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_session():
    return SessionLocal()
