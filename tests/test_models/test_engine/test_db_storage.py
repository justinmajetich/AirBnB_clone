#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.user import User
import os
from MySQLdb import _mysql

class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """
    def test_all(self):
        """ test all() function """
        new = City()
        storage.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_methods(self):
        """ test presence of methods """
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'delete'))
        self.assertTrue(hasattr(storage, 'reload'))

    def test_models(self):
        """ test of creating a models user with db """
        db=_mysql.connect("localhost", "hbnb_test", "hbnb_test_pwd", "hbnb_test_db")
        gab = User(name="Gabriel", password="zizicacamixtape", email="5652@holbertonstudents.com")
        gab.save()
        db.query("""SELECT * FROM users""")
        r=db.store_result()
        #print(len(r.fetch_row()))
        self.assertEqual(1, len(r.fetch_row()))
        sonia = User(name="Sonia", password="devops", email="sonia@holbertonstudents.com")
        sonia.save()
        db.query("""SELECT * FROM users""")
        r=db.store_result()
        #print(len(r.fetch_row(2,0)))
        self.assertEqual(2, len(r.fetch_row(2,0)))
        
if __name__ == "__main__":
    unittest.main()
