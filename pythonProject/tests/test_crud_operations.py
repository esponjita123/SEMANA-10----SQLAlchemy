import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from crud.crud_operations import CRUDOperations

class TestCRUDOperations(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.crud = CRUDOperations(self.session)

    def test_create_article(self):
        article = self.crud.create_article("Test Article")
        self.assertIsNotNone(article.id)
        self.assertEqual(article.titulo, "Test Article")

    def test_create_comment(self):
        article = self.crud.create_article("Test Article")
        comment = self.crud.create_comment("Test Comment", article)
        self.assertIsNotNone(comment.id)
        self.assertEqual(comment.comentario, "Test Comment")
        self.assertEqual(comment.article.id, article.id)

    def test_read_article(self):
        article = self.crud.create_article("Read Test")
        found_article = self.crud.read_article(article.id)
        self.assertEqual(found_article.titulo, "Read Test")

    def test_update_article(self):
        article = self.crud.create_article("Old Title")
        updated_article = self.crud.update_article(article.id, "New Title")
        self.assertEqual(updated_article.titulo, "New Title")

    def test_delete_article(self):
        article = self.crud.create_article("Delete Test")
        deleted_article = self.crud.delete_article(article.id)
        self.assertIsNone(self.crud.read_article(deleted_article.id))

if __name__ == '__main__':
    unittest.main()
