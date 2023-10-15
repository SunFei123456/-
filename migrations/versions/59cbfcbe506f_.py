"""empty message

Revision ID: 59cbfcbe506f
Revises: da4d3a39efc7
Create Date: 2023-10-11 21:41:26.022214

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '59cbfcbe506f'
down_revision = 'da4d3a39efc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_Captcha',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('email', sa.String(length=20), nullable=False),
                    sa.Column('captcha', sa.String(length=100), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    with op.batch_alter_table('questions_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions_model', schema=None) as batch_op:
        batch_op.drop_column('create_time')

    op.drop_table('email_Captcha')
    # ### end Alembic commands ###
