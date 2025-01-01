"""add descreption

Revision ID: 9ab66cc4f813
Revises: fadee8f9751c
Create Date: 2024-12-15 18:54:45.081416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ab66cc4f813'
down_revision = 'fadee8f9751c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('por', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descreption', sa.String(length=80), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('por', schema=None) as batch_op:
        batch_op.drop_column('descreption')

    # ### end Alembic commands ###
