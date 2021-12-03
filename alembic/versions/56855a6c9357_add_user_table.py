"""add user table

Revision ID: 56855a6c9357
Revises: ff6cd5ddf72a
Create Date: 2021-12-02 22:59:58.162915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56855a6c9357'
down_revision = 'ff6cd5ddf72a'
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
