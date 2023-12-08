"""Money column added in Booking classs

Revision ID: b39d5f7109c5
Revises: ba4defa9a3b5
Create Date: 2023-12-01 20:46:05.063364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b39d5f7109c5'
down_revision = 'ba4defa9a3b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('money', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_booking_money'), ['money'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_booking_money'))
        batch_op.drop_column('money')

    # ### end Alembic commands ###