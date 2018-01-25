"""add parks

Revision ID: 7428f83d1fba
Revises: 22f5f99efe66
Create Date: 2018-01-19 14:46:40.203383

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import sys
from pathlib import Path
monocle_dir = str(Path(__file__).resolve().parents[2])
if monocle_dir not in sys.path:
    sys.path.append(monocle_dir)
from monocle import db as db

# revision identifiers, used by Alembic.
revision = '7428f83d1fba'
down_revision = '22f5f99efe66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forts', 'park')
    op.add_column('forts', sa.Column('parkid', db.HUGE_TYPE, nullable=True))
    op.add_column('forts', sa.Column('park', sa.String(length=200), nullable=True))
    op.create_table('parks',
        sa.Column('id', db.HUGE_TYPE, nullable=True, unique=True),
        sa.Column('name', sa.String(length=200), nullable=True),
        sa.Column('coords', db.LONG_TEXT, nullable=True),
        sa.Column('updated', sa.Integer(), nullable=True)
    )
    op.create_index('ix_forts_parkid', 'forts', ['parkid'])
    op.create_index('ix_park', 'parks', ['id'])
    op.create_foreign_key('forts_fk_parkid', 'forts', 'parks', ['parkid'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('forts_fk_parkid', 'forts', type_='foreignkey')
    op.drop_index('ix_forts_parkid', table_name='forts')
    op.drop_index('ix_park', table_name='parks')
    op.drop_column("forts", "parkid")
    op.drop_column("forts", "park")
    op.add_column('forts', sa.Column('park', sa.String(128), nullable=True))
    op.drop_table('parks')
    # ### end Alembic commands ###
