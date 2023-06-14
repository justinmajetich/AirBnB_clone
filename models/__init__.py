#!/usr/bin/python3
"""
Resources for this package

This module instantiates the type of Storage to use for the project
"""
from os import getenv


# Create a unique storage instance for the application
storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage
storage.reload()
