from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from ...database import Base

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