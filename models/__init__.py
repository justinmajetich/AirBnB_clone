#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage
"""
from os import getenv

engine_type = getenv("HBNB_TYPE_STORAGE")

if engine_type == "db":
    print("---> Engine == db")
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    print("---> Engine != db")
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
