"""create schools table

Revision ID: a12033ee54b1
Revises: 
Create Date: 2024-05-05 13:25:09.234963

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a12033ee54b1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "schools",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(300), nullable=False),
        sa.Column("address", sa.String(500), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("schools")
