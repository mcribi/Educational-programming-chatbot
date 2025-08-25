# Class of Exercise
# Attributes: type, question, options, answer, explanation
class Exercise:
    def __init__(self, type_, question, options, answer, explanation):
        self.type = type_
        self.question = question
        self.options = options
        self.answer = answer
        self.explanation = explanation

    def is_correct(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()
