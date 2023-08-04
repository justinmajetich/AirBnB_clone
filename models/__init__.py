#!/usr/bin/python3
"""
This module instantiates an object of storage depending on type
Contains the model of all objects
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()