from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base

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

    def __repr__(self):
        return f"<Album(id={self.id}, nombre_album='{self.nombre_album}')>"