#!/usr/bin/python3
"""This module sets up the storage mechanism for the application."""
from os import getenv


# Check the value of the HBNB_TYPE_STORAGE environment variable

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Load data into the storage instance
storage.reload()
