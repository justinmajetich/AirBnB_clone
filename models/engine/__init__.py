#!/usr/bin/python3
"""Module intantiates an object of class FILESTORAGE OR DBSTORAGE"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
