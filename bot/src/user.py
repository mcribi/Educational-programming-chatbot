#class of User for identify and save data of users
# Attributes: id, name, attempts

class User:
    #constructor
    def __init__(self, telegram_id, name):
        self.id = telegram_id
        self.name = name
        self.attempts = []

    #method to register an attempt
    def register_attempt(self, attempt):
        self.attempts.append(attempt)

    # method to get the number of attempts
    def get_attempt_count(self):
        return len(self.attempts)

    # method to get the success rate of attempts
    def get_success_rate(self):
        total = len(self.attempts)
        correct = sum(1 for a in self.attempts if a.is_correct)
        return (correct / total * 100) if total > 0 else 0
