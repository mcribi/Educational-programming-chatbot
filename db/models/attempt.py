from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_correct = Column(Boolean, nullable=False)

    user = relationship("User", back_populates="attempts")
