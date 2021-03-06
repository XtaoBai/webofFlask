"""new fields in user model

Revision ID: 56530dcc0159
Revises: bd8b27416d1e
Create Date: 2019-07-15 14:57:02.312901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56530dcc0159'
down_revision = 'bd8b27416d1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
