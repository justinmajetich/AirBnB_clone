#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
    Instatiates the database storage engine (DBStorage) when the env
    var "HBNB_TYPE_STORAGE" is set to 'db'
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
