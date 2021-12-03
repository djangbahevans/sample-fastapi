"""add content column to posts table

Revision ID: ff6cd5ddf72a
Revises: 79eb11cbb477
Create Date: 2021-12-02 22:52:55.030238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff6cd5ddf72a'
down_revision = '79eb11cbb477'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
