# api/user/rating/models.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ...database import Base

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