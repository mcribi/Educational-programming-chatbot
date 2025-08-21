from db.database import SessionLocal
import db.models 
from db.models import Topic as TopicModel, Lesson as LessonModel

def populate_lessons_from_loader(load_theory_fn):
    """
      Get the function load_theory() that return:
      { "Name of the topic": src.Topic(name, lessons=[src.Lesson(title, content), ...]), ... }
      and put it in the DB (topics, lessons).
    """
    topics_dict = load_theory_fn()
    session = SessionLocal()
    try:
        #topics
        existing_topics = {
            t.name: t for t in session.query(TopicModel).all()
        }

        for topic_name, topic_obj in topics_dict.items():
            # get-or-create of Topic
            db_topic = existing_topics.get(topic_name)
            if db_topic is None:
                db_topic = TopicModel(name=topic_name)
                session.add(db_topic)
                session.flush()  # obtenemos db_topic.id
                existing_topics[topic_name] = db_topic

            # upsert of each Lesson of (topic_id, title)
            for lesson_obj in topic_obj.lessons:  # src.Lesson(title, content)
                title = lesson_obj.title.strip()
                content = lesson_obj.content

                db_lesson = (
                    session.query(LessonModel)
                    .filter(LessonModel.topic_id == db_topic.id,
                            LessonModel.title == title)
                    .first()
                )
                if db_lesson:
                    # refresh the content
                    if db_lesson.content != content:
                        db_lesson.content = content
                else:
                    session.add(LessonModel(
                        title=title,
                        content=content,
                        topic_id=db_topic.id
                    ))
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
