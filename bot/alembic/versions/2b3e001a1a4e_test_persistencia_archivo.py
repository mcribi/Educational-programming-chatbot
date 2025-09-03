"""test persistencia archivo

Revision ID: 2b3e001a1a4e
Revises: de1d1942d52a
Create Date: 2025-09-03 10:56:56.829894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b3e001a1a4e'
down_revision: Union[str, Sequence[str], None] = 'de1d1942d52a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
