#!/usr/bin/python3
"""This module sets up the storage mechanism for the application."""
import os

# Check the value of the HBNB_TYPE_STORAGE environment variable
storage_type = os.environ.get("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Load data into the storage instance
storage.reload()
