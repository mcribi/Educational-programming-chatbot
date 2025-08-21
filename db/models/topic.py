from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base  

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    lessons = relationship("Lesson", back_populates="topic", cascade="all, delete-orphan")
    exercises = relationship("Exercise", back_populates="topic", cascade="all, delete-orphan")

