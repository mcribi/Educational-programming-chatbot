# src/models/log.py

from datetime import datetime

class Log:
    def __init__(self, level, logger, message, 
                 traceback=None, module=None, func=None,
                 pathname=None, lineno=None, user_id=None, context=None, 
                 created_at=None):
        self.level = level
        self.logger = logger
        self.message = message
        self.traceback = traceback
        self.module = module
        self.func = func
        self.pathname = pathname
        self.lineno = lineno
        self.user_id = user_id
        self.context = context
        self.created_at = created_at or datetime.utcnow()

    def __repr__(self):
        return f"<Log {self.level}: {self.message[:30]}...>"
