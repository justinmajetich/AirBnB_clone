#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
depending on the value of the environment variable HBNB_TYPE_STORAGE.
"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
