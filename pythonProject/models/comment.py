from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comentario = Column(String, nullable=False)
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)

    article = relationship('Article', back_populates='comments')

    def __repr__(self):
        return f"<Comment(id={self.id}, comentario={self.comentario}, article_id={self.article_id})>"
