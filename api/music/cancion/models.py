from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...database import Base

class Genero(Base):
    __tablename__ = "genero"

    id = Column(Integer, primary_key=True, index=True, name="id_genero")
    nombre_genero = Column(String(50), nullable=False, unique=True)

    albums = relationship("Album", back_populates="genero")
    artistas_asociados = relationship("ArtistaGenero", back_populates="genero", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Genero(id={self.id}, nombre_genero='{self.nombre_genero}')>"