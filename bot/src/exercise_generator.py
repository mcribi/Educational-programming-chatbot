#class that provides methods to generate random exercises
# Attributes: exercise_db (dict of topic name with a list of Exercise)
import random

class ExerciseGenerator:
    def __init__(self, exercise_db):
        self.exercise_db = exercise_db  # dict with topic name and a list of Exercise of this topic

    def get_random_exercise(self, topic_name):
        exercises = self.exercise_db.get(topic_name, [])
        return random.choice(exercises) if exercises else None
