#!/usr/bin/python3
"""
This module instantiates an object of
class FileStorage or DBStorage depending
on the current environ variable value
"""

from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()