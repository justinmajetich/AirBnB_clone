#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE =="db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.enging.file_storage import FileStorage
    storage = FileStorage()


storage.reload()
