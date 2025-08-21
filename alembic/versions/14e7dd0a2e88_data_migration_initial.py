"""data migration initial

Revision ID: 14e7dd0a2e88
Revises: ae64d7976271
Create Date: 2025-08-21 14:00:47.413399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14e7dd0a2e88'
down_revision: Union[str, Sequence[str], None] = 'ae64d7976271'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
