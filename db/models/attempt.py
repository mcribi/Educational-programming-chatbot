from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from db.base import Base

class Attempt(Base):
    __tablename__ = "attempts" #name of the table in the db 

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    is_correct = Column(Boolean, nullable=False)

    user = relationship("User", back_populates="attempts") # in the class user there will be a atribute calls attempts
