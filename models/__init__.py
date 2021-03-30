#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

dbType = os.getenv(HBNB_TYPE_STORAGE)

if dbType == "db":
    from models.engine import DBStorage
    
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
