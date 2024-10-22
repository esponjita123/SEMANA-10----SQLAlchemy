from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)

    comments = relationship('Comment', back_populates='article', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Article(id={self.id}, titulo={self.titulo})>"
