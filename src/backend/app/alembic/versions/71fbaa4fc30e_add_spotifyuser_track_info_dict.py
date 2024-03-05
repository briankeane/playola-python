"""Add SpotifyUser track_info dict

Revision ID: 71fbaa4fc30e
Revises: e2412789c190
Create Date: 2024-03-05 00:49:53.457859

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '71fbaa4fc30e'
down_revision = 'e2412789c190'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spotifyuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spotify_display_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('spotify_user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('spotify_token_info', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('user', 'full_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_table('spotifyuser')
    # ### end Alembic commands ###
