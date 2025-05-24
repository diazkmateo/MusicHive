from sqlalchemy import Column, Integer, String, Text, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base

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