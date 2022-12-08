#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

from os import environ
from models.engine.db_storage import DBStorage


dbstorage = environ.get("HBNB_TYPE_STORAGE")

if dbstorage == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
