"""Adding Posts table

Revision ID: a95b9f4a53ab
Revises: 
Create Date: 2020-01-12 20:27:34.283823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a95b9f4a53ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.add_column('user', sa.Column('firstname', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('joined_date', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=50), nullable=True))
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DATETIME(), nullable=True))
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'joined_date')
    op.drop_column('user', 'firstname')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###