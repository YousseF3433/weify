"""add site_name

Revision ID: 218978aa801a
Revises: a6e8688723e8
Create Date: 2024-11-24 12:03:55.876692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218978aa801a'
down_revision = 'a6e8688723e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('from', schema=None) as batch_op:
        batch_op.add_column(sa.Column('site_name', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('from', schema=None) as batch_op:
        batch_op.drop_column('site_name')

    # ### end Alembic commands ###
