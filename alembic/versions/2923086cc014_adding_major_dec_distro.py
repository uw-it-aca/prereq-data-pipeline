"""Adding  major dec distro table

Revision ID: 2923086cc014
Revises: f6bf709a0031
Create Date: 2021-07-15 00:54:31.432362+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2923086cc014'
down_revision = 'f6bf709a0031'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('majordecgpadistribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gpa_distro', sa.PickleType(), nullable=True),
    sa.Column('major_program_code', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('majordecgpadistribution')
    # ### end Alembic commands ###
