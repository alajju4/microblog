"""add language to posts

Revision ID: 742cf00b1e38
Revises: 051f0adc089e
Create Date: 2021-05-20 11:25:52.815012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '742cf00b1e38'
down_revision = '051f0adc089e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
