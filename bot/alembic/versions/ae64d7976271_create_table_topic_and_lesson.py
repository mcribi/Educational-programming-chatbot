"""create table topic and lesson

Revision ID: ae64d7976271
Revises: 9063c6e4eaa5
Create Date: 2025-08-19 19:51:35.374784
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae64d7976271'
down_revision: Union[str, Sequence[str], None] = '9063c6e4eaa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema with safe data migration from exercises.topic -> exercises.topic_id."""
    # Create master tables first
    op.create_table(
        'topics',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name', name='uq_topics_name'),
    )
    op.create_index(op.f('ix_topics_id'), 'topics', ['id'], unique=False)

    op.create_table(
        'lessons',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('topic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_lessons_id'), 'lessons', ['id'], unique=False)

    # Add the new FK column as NULLABLE first (to avoid failing on existing rows)
    op.add_column('exercises', sa.Column('topic_id', sa.Integer(), nullable=True))

    # Backfill: create Topics from distinct old textual values and link exercises
    conn = op.get_bind()

    # Create Topic rows from existing distinct exercise.topic values
    #     (safe even if exercises.topic has NULLs)
    conn.execute(sa.text("""
        INSERT INTO topics (name)
        SELECT DISTINCT topic
        FROM exercises
        WHERE topic IS NOT NULL
        ON CONFLICT (name) DO NOTHING
    """))

    # Set exercises.topic_id using the new topics
    conn.execute(sa.text("""
        UPDATE exercises e
        SET topic_id = t.id
        FROM topics t
        WHERE e.topic = t.name
    """))

    # Now that data is copied, enforce NOT NULL and FK + indexes
    op.alter_column('exercises', 'topic_id', nullable=False)
    op.create_index('ix_exercises_topic_id', 'exercises', ['topic_id'], unique=False)
    op.create_index('ix_exercises_type', 'exercises', ['type'], unique=False)
    op.create_foreign_key(
        constraint_name='fk_exercises_topic_id_topics',
        source_table='exercises',
        referent_table='topics',
        local_cols=['topic_id'],
        remote_cols=['id'],
        ondelete='CASCADE',
    )

    # Drop the old textual column
    op.drop_column('exercises', 'topic')


def downgrade() -> None:
    """Downgrade schema restoring exercises.topic from exercises.topic_id."""
    # Recreate old textual column as NULLABLE to allow backfill
    op.add_column('exercises', sa.Column('topic', sa.VARCHAR(), nullable=True))

    # Backfill text topic from the FK before dropping constraints/tables
    conn = op.get_bind()
    conn.execute(sa.text("""
        UPDATE exercises e
        SET topic = t.name
        FROM topics t
        WHERE e.topic_id = t.id
    """))

    #Make it NOT NULL to match previous model
    op.alter_column('exercises', 'topic', nullable=False)

    #Drop FK and indexes, then drop the numeric column
    op.drop_constraint('fk_exercises_topic_id_topics', 'exercises', type_='foreignkey')
    op.drop_index('ix_exercises_type', table_name='exercises')
    op.drop_index('ix_exercises_topic_id', table_name='exercises')
    op.drop_column('exercises', 'topic_id')

    #Drop lessons/topics (reverse of creation)
    op.drop_index(op.f('ix_lessons_id'), table_name='lessons')
    op.drop_table('lessons')

    op.drop_index(op.f('ix_topics_id'), table_name='topics')
    op.drop_table('topics')
