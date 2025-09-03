from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    type = Column(String, nullable=False)# types: "test" and "code"
    question = Column(String, nullable=False)#statement
    options = Column(String, nullable=True)# for test type
    answer = Column(String, nullable=False)
    explanation = Column(String, nullable=True)# explanation and feedback 
    tests_json = Column(JSONB, nullable=True)# Mini-tests for code exercises {"sample":[{input,output},...], "hidden":[...]}
    hint = Column(Text, nullable=True)   #hint
    solution_code = Column(Text, nullable=True) # oficial solution
    checker = Column(String, nullable=True, default="normalized")# compare the output
    float_tol = Column(Float, nullable=True) # tolerance for the checker   
    time_limit_ms = Column(Integer, nullable=True) # execution limits
    memory_limit_mb = Column(Integer, nullable=True) 

    # relationships
    topic = relationship("Topic", back_populates="exercises")
    attempts = relationship("Attempt", back_populates="exercise") #inverse attempt

    # shortcuts
    __table_args__ = (
        Index("ix_exercises_topic_id", "topic_id"),
        Index("ix_exercises_type", "type"),
    )
