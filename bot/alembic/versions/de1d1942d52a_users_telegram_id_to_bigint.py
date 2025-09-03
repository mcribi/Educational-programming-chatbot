"""users.telegram_id to BIGINT

Revision ID: de1d1942d52a
Revises: 76bf48a510b6
Create Date: 2025-09-02 21:43:14.419109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de1d1942d52a'
down_revision: Union[str, Sequence[str], None] = '76bf48a510b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: change users.telegram_id from INT to BIGINT."""
    op.alter_column(
        'users',
        'telegram_id',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        postgresql_using='telegram_id::bigint'
    )

def downgrade() -> None:
    """Downgrade schema: revert users.telegram_id back to INT."""
    op.alter_column(
        'users',
        'telegram_id',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        postgresql_using='telegram_id::integer'
    )
