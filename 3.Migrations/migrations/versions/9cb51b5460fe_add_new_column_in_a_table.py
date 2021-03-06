"""add new column in a table

Revision ID: 9cb51b5460fe
Revises: 3506efdd9e4f
Create Date: 2018-11-27 05:08:04.024196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb51b5460fe'
down_revision = '3506efdd9e4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=80), nullable=False))
    op.create_unique_constraint("users_email_key", 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_email_key", 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
