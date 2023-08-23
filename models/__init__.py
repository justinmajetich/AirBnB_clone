#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Check the value of the environment variable HBNB_TYPE_STORAGE
storage_type = getenv("HBNB_TYPE_STORAGE")

# Conditionally create an instance of the appropriate storage class
if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage after instantiation
storage.reload()
