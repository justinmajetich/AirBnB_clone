#!/usr/bin/python3
"""
Create a unique FileStorage instance for your application
"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()