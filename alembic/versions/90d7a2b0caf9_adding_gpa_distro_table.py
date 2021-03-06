"""adding gpa distro table

Revision ID: 90d7a2b0caf9
Revises: 405ff6c18e76
Create Date: 2021-07-13 01:02:54.870383+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d7a2b0caf9'
down_revision = '405ff6c18e76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gpadistribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crs_curric_abbr', sa.String(length=6), nullable=True),
    sa.Column('crs_number', sa.SmallInteger(), nullable=True),
    sa.Column('gpa_distro', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gpadistribution')
    # ### end Alembic commands ###
