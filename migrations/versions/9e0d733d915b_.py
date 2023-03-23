"""empty message

Revision ID: 9e0d733d915b
Revises: 2619b9bc7ba7
Create Date: 2023-03-22 22:03:20.573906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e0d733d915b'
down_revision = '2619b9bc7ba7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photoer_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['photoer_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('photoer_id')

    # ### end Alembic commands ###
