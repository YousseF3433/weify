"""empty message

Revision ID: 10ed2355f12e
Revises: d79a66e9d1b5
Create Date: 2024-11-06 09:45:02.050106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10ed2355f12e'
down_revision = 'd79a66e9d1b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shor_description', sa.String(length=180), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.drop_column('shor_description')

    # ### end Alembic commands ###