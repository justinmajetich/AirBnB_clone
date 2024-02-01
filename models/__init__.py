#!/usr/bin/python3
"""
This module defines a class: `DBStorage` or `FileStorage` based on
the value of the environment variable `HBNB_TYPE_STORAGE`
"""
import os

# Detect the value of the environment variable
HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

# switch between storage type based on the environment variable
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage
storage.reload()
