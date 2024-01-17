#!/usr/bin/python3
"""This module create an object of class file storage"""
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type != "db":
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
storage.reload()
