"""empty message

Revision ID: 623379fa4f17
Revises: 75f3174ee33c
Create Date: 2018-06-11 18:00:59.823527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623379fa4f17'
down_revision = '75f3174ee33c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
