"""empty message

Revision ID: 0eae8ff80dfb
Revises: None
Create Date: 2016-04-04 20:07:23.227152

"""

# revision identifiers, used by Alembic.
revision = '0eae8ff80dfb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('userid', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'users', ['userid'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'userid')
    ### end Alembic commands ###
