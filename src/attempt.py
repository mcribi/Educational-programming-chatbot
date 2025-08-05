#Class of Attempt for save user's answers
# Attributes: user_id, exercise, user_answer, is_correct, timestamp
from datetime import datetime

class Attempt:
    def __init__(self, user_id, exercise, user_answer, is_correct, timestamp=None):
        self.user_id = user_id
        self.exercise = exercise
        self.user_answer = user_answer
        self.is_correct = is_correct
        self.timestamp = timestamp