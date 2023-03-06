#!/usr/bin/python3
"""
This module will allow you to change storage type
directly by using an environment variable
"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.filestorage import FileStorage
    storage = FileStorage()
storage.reload()
