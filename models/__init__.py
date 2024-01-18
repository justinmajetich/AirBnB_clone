#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.__classes__ import classes


storage_type = getenv('HBNB_TYPE_STORAGE', 'file')
# print("Storage Type:", storage_type)

# from models.engine.file_storage import FileStorage
# from models.engine.db_storage import DBStorage


# HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# from models.__classes__ import classes
storage.reload()
# storage_type = HBNB_TYPE_STORAGE
