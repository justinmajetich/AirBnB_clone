#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storage_db = os.getenv("HBNB_TYPE_STORAGE")
if storage_db == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
