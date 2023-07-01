#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
    storage = DBStorage()
    storage.reload()

storage = FileStorage()
storage.reload()
