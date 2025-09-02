# Class of Suggestion
# Attributes: user_id, text, created_at, resolved
class Suggestion:
    def __init__(self, user_id, text, created_at=None, resolved=False):
        self.user_id = user_id
        self.text = text
        self.created_at = created_at
        self.resolved = resolved
