"""Renewal class added

Revision ID: b840a7fe3993
Revises: f169e04f7b84
Create Date: 2024-01-26 20:17:02.449521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b840a7fe3993'
down_revision = 'f169e04f7b84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('renewal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.String(length=8), nullable=True),
    sa.Column('renewal_type', sa.String(length=50), nullable=True),
    sa.Column('renewal_date', sa.Date(), nullable=True),
    sa.Column('renewal_cost', sa.Float(), nullable=True),
    sa.Column('description', sa.String(length=160), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['car.plate'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('renewal')
    # ### end Alembic commands ###
