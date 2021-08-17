#!/usr/bin/python
"""test for DBstorage"""
from models.engine.file_storage import FileStorage
import unittest
from models.user import User
import os
from models.engine.db_storage import DBStorage
from models import storage
from unittest.case import skipIf

@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "skip if not database"
)
class test_dbstorage(unittest.TestCase):
    """class to test the db storage methode"""
    
    def setUp(cls):
        """set up test env"""
        cls.user = User()
        cls.user.first_name = "Toto"
        cls.user.last_name = "Tata"
        cls.user.password = "Titi"
        cls.user.email = "toto@mail.com"
        cls.storage = FileStorage()
        
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def testAll(self):
        """
           Test the all function in DB Storage.
        """
        obj = storage.all()
        self.assertEqual(type(obj), dict)

    def testNew(self):
        """test new"""
        for obj in storage.all(User).values():
            temp = obj
            self.assertTrue(temp is obj)

    def testReload(self):
        """
           Test reload function in DB Storage
        """
        self.user.save()
        storage.reload()
        key = self.__keyFromInstance(self.user)
        self.assertIn(key, storage.all().keys())
        # self.user.delete()
        # storage.save()

    def __keyFromInstance(self, prmInstance):
        return "{}.{}".format(prmInstance.__class__.__name__, prmInstance.id)