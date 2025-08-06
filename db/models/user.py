from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    attempts = relationship("Attempt", back_populates="user")
