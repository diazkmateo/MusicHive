from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base

class ArtistaGenero(Base):
    __tablename__ = "artista_genero"
    artista_id = Column(Integer, ForeignKey("artista.id_artista"), primary_key=True)
    genero_id = Column(Integer, ForeignKey("genero.id_genero"), primary_key=True)

    artista = relationship("Artista", back_populates="generos_asociados")
    genero = relationship("Genero", back_populates="artistas_asociados")

    def __repr__(self):
        return f"<ArtistaGenero(artista_id={self.artista_id}, genero_id={self.genero_id})>"