#!/usr/bin/python3
"""
    Creates an instance of DBStorage or FileStorage,
    using variable HBNB_TYPE_STORAGE.
"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
