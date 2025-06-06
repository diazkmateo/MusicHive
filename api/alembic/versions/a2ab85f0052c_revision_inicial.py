"""revision inicial

Revision ID: a2ab85f0052c
Revises: 
Create Date: 2025-06-06 18:55:26.371718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2ab85f0052c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artista',
    sa.Column('id_artista', sa.Integer(), nullable=False),
    sa.Column('nombre_artista', sa.String(length=50), nullable=False),
    sa.Column('fecha_formacion', sa.Date(), nullable=True),
    sa.Column('pais_origen', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id_artista'),
    sa.UniqueConstraint('nombre_artista')
    )
    op.create_index(op.f('ix_artista_id_artista'), 'artista', ['id_artista'], unique=False)
    op.create_table('genero',
    sa.Column('id_genero', sa.Integer(), nullable=False),
    sa.Column('nombre_genero', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id_genero'),
    sa.UniqueConstraint('nombre_genero')
    )
    op.create_index(op.f('ix_genero_id_genero'), 'genero', ['id_genero'], unique=False)
    op.create_table('rol',
    sa.Column('id_rol', sa.SmallInteger(), nullable=False),
    sa.Column('nombre_rol', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id_rol'),
    sa.UniqueConstraint('nombre_rol')
    )
    op.create_index(op.f('ix_rol_id_rol'), 'rol', ['id_rol'], unique=False)
    op.create_table('album',
    sa.Column('id_album', sa.Integer(), nullable=False),
    sa.Column('nombre_album', sa.String(length=50), nullable=False),
    sa.Column('fecha_salida_album', sa.Date(), nullable=True),
    sa.Column('genero_id', sa.Integer(), nullable=True),
    sa.Column('artista_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artista_id'], ['artista.id_artista'], ),
    sa.ForeignKeyConstraint(['genero_id'], ['genero.id_genero'], ),
    sa.PrimaryKeyConstraint('id_album')
    )
    op.create_index(op.f('ix_album_id_album'), 'album', ['id_album'], unique=False)
    op.create_table('artista_genero',
    sa.Column('artista_id', sa.Integer(), nullable=False),
    sa.Column('genero_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artista_id'], ['artista.id_artista'], ),
    sa.ForeignKeyConstraint(['genero_id'], ['genero.id_genero'], ),
    sa.PrimaryKeyConstraint('artista_id', 'genero_id')
    )
    op.create_table('usuario',
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('nombre_usuario', sa.String(length=20), nullable=False),
    sa.Column('contrasena_usuario', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('rol_id', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['rol_id'], ['rol.id_rol'], ),
    sa.PrimaryKeyConstraint('id_usuario'),
    sa.UniqueConstraint('nombre_usuario')
    )
    op.create_index(op.f('ix_usuario_email'), 'usuario', ['email'], unique=True)
    op.create_index(op.f('ix_usuario_id_usuario'), 'usuario', ['id_usuario'], unique=False)
    op.create_table('cancion',
    sa.Column('id_cancion', sa.Integer(), nullable=False),
    sa.Column('nombre_cancion', sa.String(length=50), nullable=False),
    sa.Column('duracion_segundos', sa.Integer(), nullable=False),
    sa.Column('numero_pista', sa.SmallInteger(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['album.id_album'], ),
    sa.PrimaryKeyConstraint('id_cancion')
    )
    op.create_index(op.f('ix_cancion_id_cancion'), 'cancion', ['id_cancion'], unique=False)
    op.create_table('coleccion',
    sa.Column('id_coleccion', sa.Integer(), nullable=False),
    sa.Column('nombre_coleccion', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_coleccion')
    )
    op.create_index(op.f('ix_coleccion_id_coleccion'), 'coleccion', ['id_coleccion'], unique=False)
    op.create_table('rating',
    sa.Column('id_rating', sa.Integer(), nullable=False),
    sa.Column('puntuacion', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.Date(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['album.id_album'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_rating')
    )
    op.create_index(op.f('ix_rating_id_rating'), 'rating', ['id_rating'], unique=False)
    op.create_table('review',
    sa.Column('id_review', sa.Integer(), nullable=False),
    sa.Column('titulo_review', sa.String(length=100), nullable=False),
    sa.Column('nota_review', sa.SmallInteger(), nullable=False),
    sa.Column('texto_review', sa.Text(), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['album.id_album'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_review')
    )
    op.create_index(op.f('ix_review_id_review'), 'review', ['id_review'], unique=False)
    op.create_table('coleccion_canciones',
    sa.Column('id_coleccion_canciones', sa.Integer(), nullable=False),
    sa.Column('coleccion_id', sa.Integer(), nullable=False),
    sa.Column('cancion_id', sa.Integer(), nullable=False),
    sa.Column('fecha_añadido', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['cancion_id'], ['cancion.id_cancion'], ),
    sa.ForeignKeyConstraint(['coleccion_id'], ['coleccion.id_coleccion'], ),
    sa.PrimaryKeyConstraint('id_coleccion_canciones')
    )
    op.create_index(op.f('ix_coleccion_canciones_id_coleccion_canciones'), 'coleccion_canciones', ['id_coleccion_canciones'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_coleccion_canciones_id_coleccion_canciones'), table_name='coleccion_canciones')
    op.drop_table('coleccion_canciones')
    op.drop_index(op.f('ix_review_id_review'), table_name='review')
    op.drop_table('review')
    op.drop_index(op.f('ix_rating_id_rating'), table_name='rating')
    op.drop_table('rating')
    op.drop_index(op.f('ix_coleccion_id_coleccion'), table_name='coleccion')
    op.drop_table('coleccion')
    op.drop_index(op.f('ix_cancion_id_cancion'), table_name='cancion')
    op.drop_table('cancion')
    op.drop_index(op.f('ix_usuario_id_usuario'), table_name='usuario')
    op.drop_index(op.f('ix_usuario_email'), table_name='usuario')
    op.drop_table('usuario')
    op.drop_table('artista_genero')
    op.drop_index(op.f('ix_album_id_album'), table_name='album')
    op.drop_table('album')
    op.drop_index(op.f('ix_rol_id_rol'), table_name='rol')
    op.drop_table('rol')
    op.drop_index(op.f('ix_genero_id_genero'), table_name='genero')
    op.drop_table('genero')
    op.drop_index(op.f('ix_artista_id_artista'), table_name='artista')
    op.drop_table('artista')
    # ### end Alembic commands ###
