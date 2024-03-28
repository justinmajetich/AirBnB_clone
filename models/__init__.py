#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

storage_engine = getenv('HBNB_TYPE_STORAGE')
if storage_engine is None:
    storage_engine = "db"

if storage_engine == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
    