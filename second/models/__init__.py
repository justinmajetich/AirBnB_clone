#!/usr/bin/python3
"""
This module instantiates an object of class DBStorage
if the environment variable HBNB_TYPE_STORAGE is equal to db,
otherwise it instantiates an object of class FileStorage
"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
