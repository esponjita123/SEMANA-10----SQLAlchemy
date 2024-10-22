from models.article import Article
from models.comment import Comment

class CRUDOperations:
    def __init__(self, session):
        self.session = session

    def create_article(self, titulo):
        article = Article(titulo=titulo)
        self.session.add(article)
        self.session.commit()
        return article

    def create_comment(self, comentario, article):
        comment = Comment(comentario=comentario, article=article)
        self.session.add(comment)
        self.session.commit()
        return comment

    def read_article(self, article_id):
        return self.session.query(Article).filter_by(id=article_id).first()

    def update_article(self, article_id, new_title):
        article = self.read_article(article_id)
        if article:
            article.titulo = new_title
            self.session.commit()
        return article

    def delete_article(self, article_id):
        article = self.read_article(article_id)
        if article:
            self.session.delete(article)
            self.session.commit()
        return article

    def read_all_articles(self):
        return self.session.query(Article).all()
