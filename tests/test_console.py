#!/usr/bin/pyhton3
""" Writing a test model for the console.py"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream

class TestHBNBCommand(unittest.TestCase):
    """Writing test for the HBNB Command"""
    
    #so specifying to skip testing of file storage when database storage is used
    @unittest.skipUnless(
        os.getenv('HBNB_TYPE_STORAGE') != 'db', 'FileStorage test')
    
    def test_my_file_storage_method(self):
        """Tests the create command with the file storage.
        """
        
        # We use the stringIO to replace the sys.stdout so any test be stored to the pout but not printed to the command prmpt
        with patch('sys.stdout', new=StringIO()) as pout:
            const = HBNBCommand()
            const.onecmd('create City name="Texas"')
            #get value from output and use the strip to remove any white trailing space
            mdl_id = pout.getvalue().strip()
            clear_stream(pout)
            const.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", pout.getvalue().strip())
            clear_stream(pout)
            const.onecmd('create User name="Teddy" age=50 height=9.1')
            mdl_id = pout.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            clear_stream(pout)
            const.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'Teddy'", pout.getvalue().strip())
            self.assertIn("'age': 50", pout.getvalue().strip())
            self.assertIn("'height': 9.1", pout.getvalue().strip())
            
            
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'DBStorage test')  
    
    def test_database_storage(self):
        
        
            
            
            
            
            
            