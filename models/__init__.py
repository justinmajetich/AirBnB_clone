#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage

    print("Inner DB")

    storage = DBStorage()
    storage.reload()
    print(storage.all())
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
