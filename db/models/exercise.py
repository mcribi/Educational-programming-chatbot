from sqlalchemy import Column, Integer, String
from db.base import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    topic = Column(String, nullable=False)
    type = Column(String, nullable=False)  # ex: test, code
    question = Column(String, nullable=False)
    options = Column(String, nullable=True)  # JSON string if multiple choice
    answer = Column(String, nullable=False)
    explanation = Column(String, nullable=True)