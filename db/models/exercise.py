from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    type = Column(String, nullable=False) 
    question = Column(String, nullable=False)
    options = Column(String, nullable=True) 
    answer = Column(String, nullable=False)
    explanation = Column(String, nullable=True)

    topic = relationship("Topic", back_populates="exercises")

    #shortcuts
    __table_args__ = (
        Index("ix_exercises_topic_id", "topic_id"),
        Index("ix_exercises_type", "type"),
    )