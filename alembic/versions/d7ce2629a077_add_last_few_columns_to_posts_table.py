"""add last few columns to posts table

Revision ID: d7ce2629a077
Revises: 3db061440762
Create Date: 2021-12-02 23:15:48.426742

"""
from datetime import time
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7ce2629a077'
down_revision = '3db061440762'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
