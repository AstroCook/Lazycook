"""create ingridients table

Revision ID: 98a2eb328f00
Revises: 8978fef71097
Create Date: 2023-02-23 21:03:26.934022

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '98a2eb328f00'
down_revision = '8978fef71097'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ingridients",
        sa.Column(
            "id",
            sa.dialects.postgresql.UUID(as_uuid=True),
            primary_key=True,
            default=UUID.uuid4,
        ),
        sa.Column(
            "date_of_creation", sa.DateTime(timezone=True), server_default=func.now()
        ),
        sa.Column("date_of_last_edit", sa.DateTime(timezone=True), onupdate=func.now()),
        sa.Column("disabled", sa.Boolean, default=False),
        sa.Column("name", sa.String),
    ),

    op.create_table(
        "ingridient_allergies",
        sa.Column("ingridient_id", UUID(as_uuid=True), sa.ForeignKey("ingridients.id")),
        sa.Column("allergy_id", UUID(as_uuid=True), sa.ForeignKey("allergies.id")),
    ),


def downgrade() -> None:
    pass
