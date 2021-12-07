"""update curric

Revision ID: 2c188851747d
Revises: 18ed3c223e3d
Create Date: 2021-11-04 23:18:44.255088+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c188851747d'
down_revision = '18ed3c223e3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curriculum', sa.Column('course_data', sa.Text(), nullable=True))
    op.drop_column('curriculum', 'postreqs')
    op.drop_column('curriculum', 'prereqs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curriculum', sa.Column('prereqs', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('curriculum', sa.Column('postreqs', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
