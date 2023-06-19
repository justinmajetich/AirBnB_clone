#!/usr/bin/python3

import os

storage_type =  os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    """Instantiates an object of class DBStorage"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    """Instantiates an object of class FileStorage"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
