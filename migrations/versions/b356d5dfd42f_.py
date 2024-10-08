"""empty message

Revision ID: b356d5dfd42f
Revises: ed8d212f4347
Create Date: 2024-10-04 20:04:10.018521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b356d5dfd42f'
down_revision = 'ed8d212f4347'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eventos', schema=None) as batch_op:
        batch_op.alter_column('data',
               existing_type=sa.DATE(),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('hora_inicio',
               existing_type=sa.TIME(),
               type_=sa.String(length=5),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eventos', schema=None) as batch_op:
        batch_op.alter_column('hora_inicio',
               existing_type=sa.String(length=5),
               type_=sa.TIME(),
               existing_nullable=True)
        batch_op.alter_column('data',
               existing_type=sa.String(length=10),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###
