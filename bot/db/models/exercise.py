from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)

    # types: "test" and "code"
    type = Column(String, nullable=False)

    #statement
    question = Column(String, nullable=False)

    # for test type
    options = Column(String, nullable=True)
    answer = Column(String, nullable=False)

    # explanation and feedback 
    explanation = Column(String, nullable=True)

    # Mini-tests for code exercises {"sample":[{input,output},...], "hidden":[...]}
    tests_json = Column(JSONB, nullable=True)

    #hint
    hint = Column(Text, nullable=True)

    # oficial solution
    solution_code = Column(Text, nullable=True)

    # compare the output
    checker = Column(String, nullable=True, default="normalized")

    # tolerance for the checker
    float_tol = Column(Float, nullable=True)

    # execution limits
    time_limit_ms = Column(Integer, nullable=True)   
    memory_limit_mb = Column(Integer, nullable=True) 

    # relationships
    topic = relationship("Topic", back_populates="exercises")
    attempts = relationship("Attempt", back_populates="exercise") #inverse attempt

    # shortcuts
    __table_args__ = (
        Index("ix_exercises_topic_id", "topic_id"),
        Index("ix_exercises_type", "type"),
    )
