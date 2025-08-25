import logging, traceback as tb
from db.database import SessionLocal 
from db.models.log import Log

class SQLAlchemyLogHandler(logging.Handler):
    def __init__(self, session_factory=SessionLocal):
        super().__init__()
        self._Session = session_factory

    def emit(self, record: logging.LogRecord):
        #never interrupt the flow of the app due to a log error
        try:
            session = self._Session()
            try:
                trace_txt = None
                if record.exc_info:
                    trace_txt = "".join(tb.format_exception(*record.exc_info))
                elif getattr(record, "exc_text", None):
                    trace_txt = record.exc_text

                # message already includes the formatter's formatter
                msg = self.format(record)

                entry = Log(
                    level    = record.levelname,
                    logger   = record.name,
                    message  = msg,
                    traceback= trace_txt,
                    module   = record.module,
                    func     = record.funcName,
                    pathname = record.pathname,
                    lineno   = record.lineno,
                    context  = getattr(record, "context", None) or getattr(record, "extra", None)
                )
                session.add(entry)
                session.commit()
            finally:
                session.close()
        except Exception:
            pass
