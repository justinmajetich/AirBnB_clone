#!/usr/bin/python3
"""create a unique FileStorage instance for your application
"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
