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

def _as_options(val):
    if val is None:
        return None
    if isinstance(val, list):
        return "|".join(val)
    return val

def populate_exercises():
    """Seed the DB with exercises from your in-memory catalog."""
    with SessionLocal() as session:
        for topic_name, exercise_list in exercises_by_topic.items():
            topic = get_or_create_topic(session, topic_name)

            for ex in exercise_list:
                # ex.type and ex.type_
                ex_type = getattr(ex, "type", getattr(ex, "type_", None))

                exists = session.query(ExerciseModel).filter_by(question=ex.question).first()

                if not exists:
                    db_ex = ExerciseModel(
                        topic_id=topic.id,
                        type=ex_type,
                        question=ex.question,

                        # test atributes
                        options=_as_options(getattr(ex, "options", None)),
                        answer=getattr(ex, "answer", None),
                        explanation=getattr(ex, "explanation", None),

                        # Programming atributes
                        tests_json=getattr(ex, "tests_json", None),
                        hint=getattr(ex, "hint", None),
                        solution_code=getattr(ex, "solution_code", None),
                        checker=getattr(ex, "checker", None),
                        time_limit_ms=getattr(ex, "time_limit_ms", None),
                        memory_limit_mb=getattr(ex, "memory_limit_mb", None),
                    )
                    session.add(db_ex)
                else:
                    # "upsert": update whatever is defined in the object in memory
                    exists.topic_id = topic.id
                    exists.type = ex_type or exists.type
                    exists.question = ex.question or exists.question

                    # Test
                    if hasattr(ex, "options"):
                        exists.options = _as_options(getattr(ex, "options", None))
                    if hasattr(ex, "answer"):
                        exists.answer = getattr(ex, "answer", None)
                    if hasattr(ex, "explanation"):
                        exists.explanation = getattr(ex, "explanation", None)

                    # code
                    if hasattr(ex, "tests_json"):
                        exists.tests_json = getattr(ex, "tests_json", None)
                    if hasattr(ex, "hint"):
                        exists.hint = getattr(ex, "hint", None)
                    if hasattr(ex, "solution_code"):
                        exists.solution_code = getattr(ex, "solution_code", None)
                    if hasattr(ex, "checker"):
                        exists.checker = getattr(ex, "checker", None)
                    if hasattr(ex, "time_limit_ms"):
                        exists.time_limit_ms = getattr(ex, "time_limit_ms", None)
                    if hasattr(ex, "memory_limit_mb"):
                        exists.memory_limit_mb = getattr(ex, "memory_limit_mb", None)

        session.commit()


if __name__ == "__main__":
    populate_exercises()