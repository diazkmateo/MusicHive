from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

### music models
class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True, name="id_album")
    nombre_album = Column(String(50), nullable=False)
    fecha_salida_album = Column(Date, nullable=True)
    genero_id = Column(Integer, ForeignKey("genero.id_genero"), nullable=True)
    artista_id = Column(Integer, ForeignKey("artista.id_artista"), nullable=False)

    genero = relationship("Genero", back_populates="albums")
    artista = relationship("Artista", back_populates="albums")
    canciones = relationship("Cancion", back_populates="album", cascade="all, delete-orphan")
    
    reviews = relationship("Review", back_populates="album")
    ratings = relationship("Rating", back_populates="album")
    # canciones = relationship("Cancion", back_populates="album")

    def __repr__(self):
        return f"<Album(id={self.id}, nombre_album='{self.nombre_album}')>"
    
class Artista(Base):
    __tablename__ = "artista"

    id = Column(Integer, primary_key=True, index=True, name="id_artista")
    nombre_artista = Column(String(50), nullable=False, unique=True)
    fecha_formacion = Column(Date, nullable=True)
    pais_origen = Column(String(20), nullable=True)

    albums = relationship("Album", back_populates="artista", cascade="all, delete-orphan")
    generos_asociados = relationship("ArtistaGenero", back_populates="artista", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Artista(id={self.id}, nombre_artista='{self.nombre_artista}')>"
    
class ArtistaGenero(Base):
    __tablename__ = "artista_genero"

    id = Column(Integer, primary_key=True, index=True, name="id_artista_genero")

    artista_id = Column(Integer, ForeignKey("artista.id_artista"), primary_key=True)
    genero_id = Column(Integer, ForeignKey("genero.id_genero"), primary_key=True)

    artista = relationship("Artista", back_populates="generos_asociados")
    genero = relationship("Genero", back_populates="artistas_asociados")

    def __repr__(self):
        return f"<ArtistaGenero(artista_id={self.artista_id}, genero_id={self.genero_id})>"
    
class Genero(Base):
    __tablename__ = "genero"

    id = Column(Integer, primary_key=True, index=True, name="id_genero")
    nombre_genero = Column(String(50), nullable=False, unique=True)

    albums = relationship("Album", back_populates="genero")
    artistas_asociados = relationship("ArtistaGenero", back_populates="genero", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Genero(id={self.id}, nombre_genero='{self.nombre_genero}')>"
    
class Cancion(Base):
    __tablename__ = "cancion"

    id = Column(Integer, primary_key=True, index=True, name="id_cancion")
    nombre_cancion = Column(String(50), nullable=False, unique=False)
    duracion_segundos = Column(Integer, nullable=False, name="duracion_segundos")
    numero_pista = Column(SmallInteger, nullable=False, name="numero_pista")

    album_id = Column(Integer, ForeignKey("album.id_album"), nullable=False)

    album = relationship("Album", back_populates="canciones")
    colecciones_asociadas = relationship("ColeccionCanciones", back_populates="cancion")

    def __repr__(self):
        return f"<Cancion(id={self.id}, nombre_cancion='{self.nombre_cancion}', duracion_segundos={self.duracion_segundos})>"



### user models
class Coleccion(Base):
    __tablename__ = "coleccion"

    id = Column(Integer, primary_key=True, index=True, name="id_coleccion")
    nombre_coleccion = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False, name="id_usuario")

    usuario = relationship("Usuario", back_populates="colecciones")
    canciones_asociadas = relationship("ColeccionCanciones", back_populates="coleccion", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Coleccion(id={self.id}, nombre_coleccion='{self.nombre_coleccion}')>"
    
class ColeccionCanciones(Base):
    __tablename__ = "coleccion_canciones"

    id = Column(Integer, primary_key=True, index=True, name="id_coleccion_canciones")
    coleccion_id = Column(Integer, ForeignKey("coleccion.id_coleccion"), nullable=False)
    cancion_id = Column(Integer, ForeignKey("cancion.id_cancion"), nullable=False)
    fecha_anadido = Column(Date, nullable=False, default=func.current_date(), name="fecha_añadido")

    coleccion = relationship("Coleccion", back_populates="canciones_asociadas")
    cancion = relationship("Cancion", back_populates="colecciones_asociadas")

    def __repr__(self):
        return f"<ColeccionCanciones(id={self.id}, coleccion_id={self.coleccion_id}, cancion_id={self.cancion_id})>"
    
class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True, name="id_rating")
    puntuacion = Column(Integer, nullable=False)
    fecha_creacion = Column(Date, nullable=False, default=func.current_date())
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    album_id = Column(Integer, ForeignKey("album.id_album"), nullable=False)

    usuario = relationship("Usuario", back_populates="ratings")
    album = relationship("Album", back_populates="ratings")

    def __repr__(self):
        return f"<Rating(id={self.id}, puntuacion={self.puntuacion})>"
    
class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True, name="id_review")
    titulo_review = Column(String(100), nullable=False)
    nota_review = Column(SmallInteger, nullable=False)
    texto_review = Column(Text, nullable=True)
    album_id = Column(Integer, ForeignKey("album.id_album"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)

    album = relationship("Album", back_populates="reviews")
    usuario = relationship("Usuario", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, titulo_review='{self.titulo_review}')>"
    
class Rol(Base):
    __tablename__ = "rol"

    id = Column(SmallInteger, primary_key=True, index=True, name="id_rol")
    nombre_rol = Column(String(50), unique=True, nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")
    def __repr__(self):
        return f"<Rol(id={self.id}, nombre_rol='{self.nombre_rol}')>"
    
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True, name="id_usuario")
    nombre_usuario = Column(String(20), nullable=False, unique=True)
    contrasena_hash = Column(String, nullable=False, name="contrasena_usuario")
    email = Column(String(50), unique=True, index=True, nullable=False)
    rol_id = Column(SmallInteger, ForeignKey("rol.id_rol"), nullable=False)

    rol = relationship("Rol", back_populates="usuarios")
        
    reviews = relationship("Review", back_populates="usuario", cascade="all, delete-orphan")
    ratings = relationship("Rating", back_populates="usuario", cascade="all, delete-orphan")
    colecciones = relationship("Coleccion", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre_usuario='{self.nombre_usuario}')>"