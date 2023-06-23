#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or Dbstorage"""
from models.engine.file_storage import FileStorage
from models.engine.dbstorage import Dbstorage
from os import getenv

store = getenv("HBNB_TYPE_STORAGE")

if store == "db":
    storage = Dbstorage()
else:
    storage = FileStorage()

storage.reload()
