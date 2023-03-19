"""empty message

Revision ID: bdbee85f639e
Revises: f337db91d2be
Create Date: 2023-03-12 14:22:16.463429

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bdbee85f639e'
down_revision = 'f337db91d2be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', mysql.VARCHAR(length=80), nullable=False))

    # ### end Alembic commands ###