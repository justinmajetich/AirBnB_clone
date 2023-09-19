#!/usr/bin/python3
"""
    This module instantiates an object of class FileStorage or DBStorage
    depending on the storage type
"""
import os


storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
