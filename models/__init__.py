#!/usr/bin/python3

from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    """Instantiates an object of class DBStorage"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    """Instantiates an object of class FileStorage"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
