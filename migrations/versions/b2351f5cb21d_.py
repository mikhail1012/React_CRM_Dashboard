"""empty message

Revision ID: b2351f5cb21d
Revises: 5d0e968a59f2
Create Date: 2019-11-08 23:40:11.266255

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b2351f5cb21d'
down_revision = '5d0e968a59f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaigns', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mailer_file', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('job_number', sa.String(length=25), nullable=False))
        batch_op.add_column(sa.Column('mailing_date', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('offer_expire_date', sa.String(length=10), nullable=False))
        batch_op.create_unique_constraint('job_number', ['job_number'])
        batch_op.create_unique_constraint('mailer_file', ['mailer_file'])
        batch_op.alter_column('public_id',
                              existing_type=sa.VARCHAR(length=100),
                              nullable=True)

    with op.batch_alter_table('candidate_imports', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=100), nullable=False))
        batch_op.create_unique_constraint('public_id', ['public_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('candidate_imports', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('public_id')

    with op.batch_alter_table('campaigns', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('offer_expire_date')
        batch_op.drop_column('mailing_date')
        batch_op.drop_column('job_number')
        batch_op.alter_column('public_id',
                              existing_type=sa.VARCHAR(length=100),
                              nullable=False)

    # ### end Alembic commands ###
