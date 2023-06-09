"""empty message

Revision ID: fb6cacdd482b
Revises: 
Create Date: 2023-03-30 11:27:50.240620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb6cacdd482b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('villain',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('villain', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('hero', sa.String(length=200), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('villain')
    op.drop_table('user')
    # ### end Alembic commands ###
