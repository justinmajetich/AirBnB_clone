#!/usr/bin/python3
"""
	Testing databsase
"""
import time
import unittest
import sys
from models.engine.db_storage import DBStorage
from models import storage
from models.user import User
from models.state import State
from models import storage
from console import HBNBCommand
from os import getenv
from io import StringIO

db = getenv("HBNB_TYPE_STORAGE")

@unittest.skipIf(db != 'db', "Testing DBstorage only")
class TestDBStorage(unittest.TestCase):
     """
	 	Storage class
	 """
     @classmethod
     def setUpClass(cls):
         """
		 	initializing class
         """
         cls.dbstorage = DBStorage()
         cls.output = StringIO()
         sys.stdout = cls.output

     @classmethod
     def tearDownClass(cls:
	  	 """
              delete variables
         """
         del cls.dbstorage
         del cls.output

     def create(self):
          """
		  	Create HBNBCommand()
          """
		  return HBNBCommand()

     def test_new(self):
          """
             Test DB new
          """
		  new_obj = State(name="California")
          self.assertEqual(new_obj.name, "California")

     def test_dbstorage_user_attr(self):
          """
             Testing user attributes
          """
		  new = User(email="melissa@hbtn.com", password="hello"
		  self.assertTrue(new.email, "melissa@hbtn.com")

     def test_dbstorage_check_method(self):
	  	  """
		  	Checks if method exists
          """
          self.assertTrue(hasattr(self.dbstorage, "all"))
          self.assertTrue(hasattr(self.dbstorage, "__init__"))
          self.assertTrue(hasattr(self.dbstorage, "new"))
		  self.assertTrue(hasattr(self.dbstorage, "save"))
		  self.assertTrue(hasattr(self.dbstorage, "delete"))
		  self.assertTrue(hasattr(self.dbstorage, "reload"))

     def test_dbstorage_all(self):
          """
             Testing all functions
          """
          storage.reload()
          result = storage.all("")
          self.assertIsInstance(result, dict)
          self.assertEqual(len(result), 0)
		  new = User(email="lina@hbtn.com", password="abc")
		  console = self.create()
          console.onecmd("create State name=California")
          result = storage.all("State")
          self.assertTrue(len(result) > 0)

     def test_dbstorage_new_save(self):
          """
             testing save method
		  """
          new_state = State(name="NewYork")
          storage.new(new_state)
		  save_id = new_state.id
          result = storage.all("State")
          temp_list = []
          for k, v in result.items():
              temp_list.append(k.split('.')[1])
              obj = v
          self.assertTrue(save_id in temp_list)
          self.assertIsInstance(obj, State)

     def test_dbstorage_delete(self):
          """
             test for deketion
          """
          new_user = User(email="amayeboah@gmail.com", password="xyz",
		                  first_name="Adriel", last_name="Tolentino")
          storage.new(new_user)
          save_id = new_user.id
          key = "User.{}".format(save_id)
          self.assertIsInstance(new_user, User)
          storage.save()
          old_result = storage.all("User")
          del_user_obj = old_result[key]
          storage.delete(del_user_obj)
          new_result = storage.all("User")
          self.assertNotEqual(len(old_result), len(new_result))

     def test_model_storage(self):
          self.assertTrue(isinstance(storage, DBStorage))
