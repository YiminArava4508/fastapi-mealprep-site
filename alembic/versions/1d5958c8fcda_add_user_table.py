"""add user table

Revision ID: 1d5958c8fcda
Revises: 981b092d8894
Create Date: 2023-05-15 20:16:06.174951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d5958c8fcda'
down_revision = '981b092d8894'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                              sa.PrimaryKeyConstraint('id'),
                              sa.UniqueConstraint('email')
    )
    pass

def downgrade():
    op.drop_table('users')
    pass
