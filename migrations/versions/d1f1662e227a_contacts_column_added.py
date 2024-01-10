"""Contacts Column Added

Revision ID: d1f1662e227a
Revises: 7aafc53f9fcf
Create Date: 2024-01-10 15:42:07.068603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f1662e227a'
down_revision = '7aafc53f9fcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=8), nullable=True),
    sa.Column('driver_licence_n', sa.Integer(), nullable=True),
    sa.Column('dob', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_contacts_dob'), ['dob'], unique=False)
        batch_op.create_index(batch_op.f('ix_contacts_driver_licence_n'), ['driver_licence_n'], unique=False)
        batch_op.create_index(batch_op.f('ix_contacts_full_name'), ['full_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_contacts_full_name'))
        batch_op.drop_index(batch_op.f('ix_contacts_driver_licence_n'))
        batch_op.drop_index(batch_op.f('ix_contacts_dob'))

    op.drop_table('contacts')
    # ### end Alembic commands ###
