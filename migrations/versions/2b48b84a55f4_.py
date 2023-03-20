"""empty message

Revision ID: 2b48b84a55f4
Revises: 0efbf011deb0
Create Date: 2023-03-19 16:46:29.638472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b48b84a55f4'
down_revision = '0efbf011deb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=128), nullable=False),
    sa.Column('Filename', sa.String(length=128), nullable=False),
    sa.Column('Description', sa.String(length=500), nullable=False),
    sa.Column('Upload_time', sa.DateTime(), nullable=False),
    sa.Column('Image_path', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photos')
    # ### end Alembic commands ###
