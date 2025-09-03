# db/models/log.py
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from db.base import Base

class Log(Base):
    __tablename__ = "app_logs"

    id         = sa.Column(sa.BigInteger, primary_key=True)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False)
    level      = sa.Column(sa.String(20), nullable=False)      # DEBUG/INFO/WARNING/ERROR/CRITICAL
    logger     = sa.Column(sa.String(100), nullable=False)     # name of the logger
    message    = sa.Column(sa.Text, nullable=False)
    traceback  = sa.Column(sa.Text, nullable=True)             # stack trace si lo hay
    module     = sa.Column(sa.String(200), nullable=True)
    func       = sa.Column(sa.String(200), nullable=True)
    pathname   = sa.Column(sa.String(500), nullable=True)
    lineno     = sa.Column(sa.Integer, nullable=True)
    user_id    = sa.Column(sa.Integer, sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True,)
    context    = sa.Column(JSONB, nullable=True)       

    user = relationship("User", foreign_keys=[user_id], passive_deletes=True)     

    __table_args__ = (
        sa.Index("ix_app_logs_created_at", "created_at"),
        sa.Index("ix_app_logs_level", "level"),
        sa.Index("ix_app_logs_logger", "logger"),
        sa.Index("ix_app_logs_context_gin", context, postgresql_using="gin"),
    )
