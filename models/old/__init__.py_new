#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv, environ

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if "HBNB_TYPE_STORAGE" in environ.keys() and \
        getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
