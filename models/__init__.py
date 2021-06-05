#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import db_storage
    storage = db_storage()
    storage.reload()

else:
    storage = FileStorage()
    storage.reload()
