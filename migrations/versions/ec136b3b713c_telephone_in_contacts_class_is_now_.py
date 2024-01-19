"""Telephone in Contacts class is now string

Revision ID: ec136b3b713c
Revises: eb7ec4b2edfd
Create Date: 2024-01-19 13:50:35.843372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec136b3b713c'
down_revision = 'eb7ec4b2edfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('telephone',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('telephone',
               existing_type=sa.String(length=20),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
