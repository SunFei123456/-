"""empty message

Revision ID: e307b583d391
Revises: 171747dccec3
Create Date: 2023-10-11 09:56:10.420751

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e307b583d391'
down_revision = '171747dccec3'
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_Captcha')
    # ### end Alembic commands ###