#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
elif getenv("HBNB_TYPE_STORAGE") == "file":
    storage = FileStorage()
else:
    print("HBNB_TYPE_STORAGE should be set to 'db' or 'file'")
    exit()
storage.reload()
