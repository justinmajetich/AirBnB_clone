#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storage = FileStorage()
storage.reload()
# Retrieve the value of the environment variable.
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    # creates an instance of the `DBStorage` class
    # and assigns it to `storage`
else:
    storage = FileStorage()
    # creates an instance of the `FileStorage` class
    # and assigns it to `storage`
storage.reload()
