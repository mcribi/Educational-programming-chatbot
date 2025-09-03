"""noop migration to skip duplicate app_logs creation

Revision ID: 76bf48a510b6
Revises: 8b011f1883e2
Create Date: 2025-08-21 18:42:57.064729
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '76bf48a510b6'
down_revision: Union[str, Sequence[str], None] = '8b011f1883e2'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Skip duplicate app_logs creation.
    pass

def downgrade() -> None:
    # Nothing to undo.
    pass
