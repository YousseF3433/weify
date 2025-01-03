"""empty message

Revision ID: 732d260b3a28
Revises: ede0eca93d7e
Create Date: 2024-12-23 22:49:30.685774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '732d260b3a28'
down_revision = 'ede0eca93d7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('por', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_src', sa.String(length=60), nullable=True))
        batch_op.drop_column('descreption')
        batch_op.drop_column('img_scr')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('por', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_scr', sa.VARCHAR(length=60), nullable=True))
        batch_op.add_column(sa.Column('descreption', sa.VARCHAR(length=80), nullable=True))
        batch_op.drop_column('img_src')

    # ### end Alembic commands ###
