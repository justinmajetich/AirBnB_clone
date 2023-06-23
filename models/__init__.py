#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or Dbstorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

store = getenv("HBNB_TYPE_STORAGE")

if store == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
