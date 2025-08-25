from db.database import SessionLocal
from db.models.exercise import Exercise as ExerciseModel
from data.exercises import exercises_by_topic
from db.models.topic import Topic

def get_or_create_topic(session, name: str) -> Topic:
    """Return a Topic row for given name, creating it if needed."""
    topic = session.query(Topic).filter_by(name=name).first()
    if not topic:
        topic = Topic(name=name)
        session.add(topic)
        session.flush()  # get topic.id without full commit
    return topic

def populate_exercises():
    """Seed the DB with exercises from your in-memory catalog."""
    with SessionLocal() as session:
        for topic_name, exercise_list in exercises_by_topic.items():
            topic = get_or_create_topic(session, topic_name)

            for ex in exercise_list:
                exists = session.query(ExerciseModel).filter_by(question=ex.question).first()
                if exists:
                    continue

                db_ex = ExerciseModel(
                    topic_id=topic.id,              
                    type=ex.type,
                    question=ex.question,
                    options="|".join(ex.options) if isinstance(ex.options, list) else ex.options,
                    answer=ex.answer,
                    explanation=ex.explanation,
                )
                session.add(db_ex)

        session.commit()
if __name__ == "__main__":
    populate_exercises()