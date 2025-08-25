#Class of Topic that contains lessons and exercises
# Attributes: name, lessons, exercises
class Topic:
    #constructor
    def __init__(self, name, lessons=None, exercises=None):
        self.name = name
        self.lessons = lessons or []
        self.exercises = exercises or []

    # method to add a lesson to the topic
    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    # method to add an exercise to the topic
    def add_exercise(self, exercise):
        self.exercises.append(exercise)
