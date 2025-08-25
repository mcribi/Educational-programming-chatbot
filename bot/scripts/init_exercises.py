from db.database import SessionLocal
from db.models.exercise import Exercise as ExerciseModel
from data.exercises import exercises_by_topic

# function to incitialize the exercises in the database
def populate_exercises():
    with SessionLocal() as session: # Create a new session
        for topic, exercises in exercises_by_topic.items():
            for ex in exercises:
                #check if the exercise already exists
                exists = session.query(ExerciseModel).filter_by(question=ex.question).first()
                if not exists: #if it does not exist, insert it
                    db_ex = ExerciseModel(
                        question=ex.question,
                        type=ex.type,
                        topic=topic,
                        options="|".join(ex.options), 
                        answer=ex.answer,
                        explanation=ex.explanation
                    )
                    session.add(db_ex) #add the exercise to the session
        session.commit() #save the changes
        #print(" Ejercicios insertados correctamente.")

if __name__ == "__main__":
    populate_exercises()