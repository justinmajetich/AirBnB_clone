#!/usr/bin/python3
"""This module instantiates DBStorage and stores it in the variable storage
    (the line storage.reload(), else an object of class FileStorage."""
from models.engine.file_storage import FileStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
