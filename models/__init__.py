#!/usr/bin/python3
"""This module instantiates an object of class FileStorage/DBStorage,
depending on the storage type,
as specified by the environment variable ``HBNB_TYPE_STORAGE``"""

from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE", "Storage type not set")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
