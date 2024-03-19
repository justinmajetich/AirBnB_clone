import unittest
from unittest.mock import patch

from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):

    def test_all(self):
        with patch(
                'models.engine.db_storage.DBStorage._DBStorage__session.query'
        ) as mock_query:
            mock_query.return_value = [BaseModel(), BaseModel()]
            storage = DBStorage()
            all_objs = storage.all()
            self.assertEqual(len(all_objs), 2)

    def test_new(self):
        storage = DBStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(obj, storage._DBStorage__session.new)

    def test_save(self):
        with patch(
                'models.engine.db_storage.DBStorage._DBStorage__session.commit'
        ) as mock_commit:
            storage = DBStorage()
            storage.save()
            mock_commit.assert_called()

    def test_delete(self):
        storage = DBStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.delete(obj)
        self.assertNotIn(obj, storage._DBStorage__session)

    def test_reload(self):
        storage = DBStorage()
        with patch(
                'models.engine.db_storage.DBStorage._DBStorage__session.remove'
        ) as mock_remove:
            storage.reload()
            mock_remove.assert_called()

    def test_close(self):
        storage = DBStorage()
        with patch(
                'models.engine.db_storage.DBStorage._DBStorage__session.remove'
        ) as mock_remove:
            storage.close()
            mock_remove.assert_called()
