"""removing incentive column from Departments Model

Revision ID: 5ecb451cb41a
Revises: f4f475b38c37
Create Date: 2022-07-17 17:51:16.416625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ecb451cb41a'
down_revision = 'f4f475b38c37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('departments', 'incentive')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('incentive', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###