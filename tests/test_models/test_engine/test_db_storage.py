"""
Unittests for db storage.
"""

import unittest
import os
import MySQLdb
import pep8
from models.engine import db_storage
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel, Base


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 'File Storage is being used.')
class TestDBStorage(unittest.TestCase):
    """Tests DBStorage"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        self.assertIsNotNone(db_storage.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.__init__.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.all.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.new.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.save.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.delete.__doc__)
        self.assertIsNotNone(db_storage.DBStorage.reload.__doc__)

    def test_following_pep8(self):
        """Tests if the code follows pep8 style guide"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/engine/db_storage.py'])

        self.assertEqual(result.total_errors, 0, 'Found style errors.')

    def test_new_row(self):
        """Tests adding a row in a table"""

        self.db_user = os.getenv('HBNB_MYSQL_USER')
        self.db_pwd = os.getenv('HBNB_MYSQL_PWD')
        self.db_host = os.getenv('HBNB_MYSQL_HOST')
        self.db_name = os.getenv('HBNB_MYSQL_DB')

        self.db = MySQLdb.connect(
            user=self.db_user,
            passwd=self.db_pwd,
            db=self.db_name,
            host=self.db_host,
            charset='utf8')

        self.cursor = self.db.cursor()
        self.storage = db_storage.DBStorage()
        self.storage.reload()

        self.cursor.execute('SELECT * FROM states')
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 0)

        state = State(name='Cairo')
        state.save()
        self.db.autocommit(True)

        self.cursor.execute('SELECT * FROM states')
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 1)

        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    unittest.main()
