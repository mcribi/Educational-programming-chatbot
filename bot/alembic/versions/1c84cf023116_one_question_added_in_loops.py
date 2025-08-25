"""one question added in loops

Revision ID: 1c84cf023116
Revises: 14e7dd0a2e88
Create Date: 2025-08-21 14:14:48.117059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text
import json


# revision identifiers, used by Alembic.
revision: str = '1c84cf023116'
down_revision: Union[str, Sequence[str], None] = '14e7dd0a2e88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

#data 
TOPIC_NAME = "Bucles"

#attributes of the class Exercise
QUESTION_TEXT = (
    "¿Qué hace este código?\n"
    "<pre><code>int i = 0;\nwhile (i < 3) {\n    cout << i;\n    i += 2;\n}</code></pre>"
)
OPTIONS_LIST = ["Imprime 0 1 2", "Imprime 0 2", "Imprime 1 3", "No imprime nada"]
ANSWER_TEXT = "Imprime 0 2"
EXPLANATION_TEXT = "El contador aumenta de 2 en 2, por lo que imprime 0 y 2."


#function to get the topic id that we insert
#conn is the conexion and topic_name is the topic that we search
def _get_topic_id(conn, topic_name):
    row = conn.execute(
        text("SELECT id FROM topics WHERE name = :name"),
        {"name": topic_name}
    ).fetchone()
    if row:
        return row[0]
    #if doesn't exist, we throw an exception
    raise ValueError(f"El tema '{topic_name}' no existe en la tabla 'topics'. "
                     f"Crea primero el topic antes de añadir ejercicios.")

def upgrade():
    conn = op.get_bind()  # connection to db

    topic_id = _get_topic_id(conn, TOPIC_NAME)  # obtain the topic

    # we store options as serialised JSON in text
    options_json = json.dumps(OPTIONS_LIST, ensure_ascii=False)

    # Build the statement and type the bind parameters to avoid AmbiguousParameter
    stmt = text("""
        INSERT INTO exercises (topic_id, "type", question, options, answer, explanation)
        SELECT :topic_id, :type, :question, :options, :answer, :explanation
        WHERE NOT EXISTS (
            SELECT 1 FROM exercises
            WHERE topic_id = :topic_id
              AND "type" = :type
              AND question = :question
        )
    """).bindparams(
        sa.bindparam("topic_id",    type_=sa.Integer()),
        sa.bindparam("type",        type_=sa.String()),
        sa.bindparam("question",    type_=sa.String()),
        sa.bindparam("options",     type_=sa.String()),
        sa.bindparam("answer",      type_=sa.String()),
        sa.bindparam("explanation", type_=sa.String()),
    )

    conn.execute(
        stmt,
        {
            "topic_id": topic_id,
            "type": "test",
            "question": QUESTION_TEXT,
            "options": options_json,
            "answer": ANSWER_TEXT,
            "explanation": EXPLANATION_TEXT,
        }
    )


def downgrade():
    conn = op.get_bind()
    topic_id = _get_topic_id(conn, TOPIC_NAME)

    # Delete the question inserted
    stmt_del = text("""
        DELETE FROM exercises
        WHERE topic_id = :topic_id
          AND "type" = :type
          AND question = :question
    """).bindparams( #for consistence of types
        sa.bindparam("topic_id", type_=sa.Integer()),
        sa.bindparam("type",     type_=sa.String()),
        sa.bindparam("question", type_=sa.String()),
    )

    conn.execute(
        stmt_del,
        {
            "topic_id": topic_id,
            "type": "test",
            "question": QUESTION_TEXT,
        }
    )
