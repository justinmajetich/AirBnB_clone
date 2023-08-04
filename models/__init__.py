#!/usr/bin/python3
"""
This module initializes the storage module based on the environment variable
HBNB_TYPE_STORAGE.
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
