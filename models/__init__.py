#!/usr/bin/python3
"""
This module will allow you to change storage type
directly by using an environment variable
"""
from os import getenv

storage = None
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

if(storage):
    storage.reload()
