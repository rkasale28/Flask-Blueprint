"""empty message

Revision ID: b82325321b91
Revises: a0721d9e8dee
Create Date: 2020-06-05 11:52:08.949801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b82325321b91'
down_revision = 'a0721d9e8dee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('student_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'student', ['student_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'student_id')
    # ### end Alembic commands ###
