"""add index to blog

Revision ID: 1578a540f2dc
Revises: c390bf413bd9
Create Date: 2024-12-22 14:12:07.598798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1578a540f2dc'
down_revision = 'c390bf413bd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('index', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.drop_column('index')

    # ### end Alembic commands ###