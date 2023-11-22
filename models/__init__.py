#!/usr/bin/python3
"""This module allows switching of storage types"""
from models.engine.file_storage import FileStorage
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
