#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

# from models.base_model import BaseModel, Base
from os import getenv


"""
This module creates an instance of a FileStorage class object.
"""
storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
