"""admin_table_setup

Revision ID: 8978fef71097
Revises: 
Create Date: 2022-12-13 23:03:54.518648

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '8978fef71097'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.dialects.postgresql.UUID, primary_key=True, default=uuid4),
        sa.Column('date_of_creation', sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column('date_of_last_edit', sa.DateTime(timezone=True), onupdate=func.now()),
        sa.Column('disabled', sa.Boolean, default=False),
        sa.Column('username', UUID, sa.ForeignKey("users.id")),
        sa.Column('name', sa.String),
        sa.Column('surname', sa.String),
        sa.Column('password', sa.String),
        sa.Column('description', sa.String),
        sa.Column('avatar_url', sa.String),
    ),

    op.create_table(
        'admins',
        sa.Column('id', sa.dialects.postgresql.UUID, primary_key=True, default=uuid4),
        sa.Column('date_of_creation', sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column('date_of_last_edit', sa.DateTime(timezone=True), onupdate=func.now()),
        sa.Column('disabled', sa.Boolean, default=False),
        sa.Column('user_id', UUID, sa.ForeignKey("users.id")),
        sa.Column('access_level', sa.Integer),
    ),

    op.create_table(
        'allergies',
        sa.Column('id', sa.dialects.postgresql.UUID, primary_key=True, default=uuid4),
        sa.Column('date_of_creation', sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column('date_of_last_edit', sa.DateTime(timezone=True), onupdate=func.now()),
        sa.Column('disabled', sa.Boolean, default=False),
        sa.Column('name', sa.String),
    ),

    op.create_table(
        'user_allergies',
        sa.Column('id', sa.dialects.postgresql.UUID, primary_key=True, default=uuid4),
        sa.Column('date_of_creation', sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column('date_of_last_edit', sa.DateTime(timezone=True), onupdate=func.now()),
        sa.Column('disabled', sa.Boolean, default=False),
        sa.Column('user_id', UUID, ForeignKey("users.id")),
        sa.Column('allergy_id', UUID, ForeignKey("allergies.id")),
        )

def downgrade() -> None:
    pass