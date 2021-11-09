"""rebuild tables

Revision ID: 6aa5ec118959
Revises: 
Create Date: 2021-10-27 20:50:09.912274+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa5ec118959'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commoncoursemajor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('major', sa.String(length=6), nullable=True),
    sa.Column('course_counts', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commonmajorforcourse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crs_curric_abbr', sa.String(length=6), nullable=True),
    sa.Column('crs_number', sa.SmallInteger(), nullable=True),
    sa.Column('major_courts', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commonmajorforcourse_crs_curric_abbr'), 'commonmajorforcourse', ['crs_curric_abbr'], unique=False)
    op.create_index(op.f('ix_commonmajorforcourse_crs_number'), 'commonmajorforcourse', ['crs_number'], unique=False)
    op.create_table('concurrentcourses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_abbrev', sa.String(length=6), nullable=True),
    sa.Column('course_number', sa.SmallInteger(), nullable=True),
    sa.Column('registration_count', sa.Integer(), nullable=True),
    sa.Column('concurrent_courses', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('concurrentcoursesmajor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('major_id', sa.String(length=6), nullable=True),
    sa.Column('concurrent_courses', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('major_id'),
    sa.UniqueConstraint('major_id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_abbrev', sa.String(length=6), nullable=True),
    sa.Column('course_number', sa.SmallInteger(), nullable=True),
    sa.Column('course_college', sa.String(length=1), nullable=True),
    sa.Column('long_course_title', sa.String(length=120), nullable=True),
    sa.Column('course_branch', sa.SmallInteger(), nullable=True),
    sa.Column('course_cat_omit', sa.Boolean(), nullable=True),
    sa.Column('diversity_crs', sa.Boolean(), nullable=True),
    sa.Column('english_comp', sa.Boolean(), nullable=True),
    sa.Column('indiv_society', sa.Boolean(), nullable=True),
    sa.Column('natural_world', sa.Boolean(), nullable=True),
    sa.Column('qsr', sa.Boolean(), nullable=True),
    sa.Column('vis_lit_perf_arts', sa.Boolean(), nullable=True),
    sa.Column('writing_crs', sa.Boolean(), nullable=True),
    sa.Column('min_credits', sa.Float(precision=4), nullable=True),
    sa.Column('max_credits', sa.Float(precision=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('curriculum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('abbrev', sa.String(length=6), nullable=True),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('campus', sa.SmallInteger(), nullable=True),
    sa.Column('url', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gpadistribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crs_curric_abbr', sa.String(length=6), nullable=True),
    sa.Column('crs_number', sa.SmallInteger(), nullable=True),
    sa.Column('gpa_distro', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('major',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_code', sa.String(length=25), nullable=True),
    sa.Column('program_title', sa.String(length=300), nullable=True),
    sa.Column('program_department', sa.String(length=300), nullable=True),
    sa.Column('program_description', sa.Text(), nullable=True),
    sa.Column('program_level', sa.String(length=25), nullable=True),
    sa.Column('program_type', sa.String(length=25), nullable=True),
    sa.Column('program_school_or_college', sa.String(length=300), nullable=True),
    sa.Column('program_dateStartLabel', sa.String(length=25), nullable=True),
    sa.Column('program_dateEndLabel', sa.String(length=25), nullable=True),
    sa.Column('campus_name', sa.String(length=12), nullable=True),
    sa.Column('program_admissionType', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('majordecgpadistribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gpa_distro', sa.PickleType(), nullable=True),
    sa.Column('major_program_code', sa.String(length=25), nullable=True),
    sa.Column('is_2yr', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prereq',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pr_and_or', sa.String(length=1), nullable=True),
    sa.Column('pr_concurrency', sa.String(length=1), nullable=True),
    sa.Column('pr_cr_s', sa.String(length=1), nullable=True),
    sa.Column('pr_grade_min', sa.String(length=2), nullable=True),
    sa.Column('pr_group_no', sa.SmallInteger(), nullable=True),
    sa.Column('pr_seq_no', sa.SmallInteger(), nullable=True),
    sa.Column('department_abbrev', sa.String(length=6), nullable=True),
    sa.Column('course_number', sa.SmallInteger(), nullable=True),
    sa.Column('pr_curric_abbr', sa.String(length=6), nullable=True),
    sa.Column('pr_course_no', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('regismajor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_key', sa.Integer(), nullable=True),
    sa.Column('regis_yr', sa.SmallInteger(), nullable=True),
    sa.Column('regis_qtr', sa.SmallInteger(), nullable=True),
    sa.Column('regis_term', sa.SmallInteger(), nullable=True),
    sa.Column('regis_pathway', sa.SmallInteger(), nullable=True),
    sa.Column('regis_branch', sa.SmallInteger(), nullable=True),
    sa.Column('regis_deg_level', sa.SmallInteger(), nullable=True),
    sa.Column('regis_deg_type', sa.SmallInteger(), nullable=True),
    sa.Column('regis_major_abbr', sa.String(length=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_regismajor_regis_term'), 'regismajor', ['regis_term'], unique=False)
    op.create_index(op.f('ix_regismajor_system_key'), 'regismajor', ['system_key'], unique=False)
    op.create_table('registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_key', sa.Integer(), nullable=True),
    sa.Column('regis_yr', sa.SmallInteger(), nullable=True),
    sa.Column('regis_qtr', sa.SmallInteger(), nullable=True),
    sa.Column('regis_term', sa.SmallInteger(), nullable=True),
    sa.Column('crs_curric_abbr', sa.String(length=6), nullable=True),
    sa.Column('crs_number', sa.SmallInteger(), nullable=True),
    sa.Column('grade', sa.String(length=2), nullable=True),
    sa.Column('gpa', sa.SmallInteger(), nullable=True),
    sa.Column('course_id', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_registration_course_id'), 'registration', ['course_id'], unique=False)
    op.create_index(op.f('ix_registration_crs_curric_abbr'), 'registration', ['crs_curric_abbr'], unique=False)
    op.create_index(op.f('ix_registration_crs_number'), 'registration', ['crs_number'], unique=False)
    op.create_index(op.f('ix_registration_regis_qtr'), 'registration', ['regis_qtr'], unique=False)
    op.create_index(op.f('ix_registration_regis_term'), 'registration', ['regis_term'], unique=False)
    op.create_index(op.f('ix_registration_regis_yr'), 'registration', ['regis_yr'], unique=False)
    op.create_index(op.f('ix_registration_system_key'), 'registration', ['system_key'], unique=False)
    op.create_table('srmajor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('major_abbr', sa.String(length=6), nullable=True),
    sa.Column('major_home_url', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_key', sa.Integer(), nullable=True),
    sa.Column('major_abbr', sa.String(length=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transcript',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_key', sa.Integer(), nullable=True),
    sa.Column('tran_yr', sa.SmallInteger(), nullable=True),
    sa.Column('tran_qtr', sa.SmallInteger(), nullable=True),
    sa.Column('combined_qtr', sa.SmallInteger(), nullable=True),
    sa.Column('qtr_grade_points', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('qtr_graded_attmp', sa.Numeric(precision=3, scale=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transcript_combined_qtr'), 'transcript', ['combined_qtr'], unique=False)
    op.create_index(op.f('ix_transcript_qtr_graded_attmp'), 'transcript', ['qtr_graded_attmp'], unique=False)
    op.create_index(op.f('ix_transcript_system_key'), 'transcript', ['system_key'], unique=False)
    op.create_table('graph',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('graph_json', sa.Text(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('graph')
    op.drop_index(op.f('ix_transcript_system_key'), table_name='transcript')
    op.drop_index(op.f('ix_transcript_qtr_graded_attmp'), table_name='transcript')
    op.drop_index(op.f('ix_transcript_combined_qtr'), table_name='transcript')
    op.drop_table('transcript')
    op.drop_table('student')
    op.drop_table('srmajor')
    op.drop_index(op.f('ix_registration_system_key'), table_name='registration')
    op.drop_index(op.f('ix_registration_regis_yr'), table_name='registration')
    op.drop_index(op.f('ix_registration_regis_term'), table_name='registration')
    op.drop_index(op.f('ix_registration_regis_qtr'), table_name='registration')
    op.drop_index(op.f('ix_registration_crs_number'), table_name='registration')
    op.drop_index(op.f('ix_registration_crs_curric_abbr'), table_name='registration')
    op.drop_index(op.f('ix_registration_course_id'), table_name='registration')
    op.drop_table('registration')
    op.drop_index(op.f('ix_regismajor_system_key'), table_name='regismajor')
    op.drop_index(op.f('ix_regismajor_regis_term'), table_name='regismajor')
    op.drop_table('regismajor')
    op.drop_table('prereq')
    op.drop_table('majordecgpadistribution')
    op.drop_table('major')
    op.drop_table('gpadistribution')
    op.drop_table('curriculum')
    op.drop_table('course')
    op.drop_table('concurrentcoursesmajor')
    op.drop_table('concurrentcourses')
    op.drop_index(op.f('ix_commonmajorforcourse_crs_number'), table_name='commonmajorforcourse')
    op.drop_index(op.f('ix_commonmajorforcourse_crs_curric_abbr'), table_name='commonmajorforcourse')
    op.drop_table('commonmajorforcourse')
    op.drop_table('commoncoursemajor')
    # ### end Alembic commands ###