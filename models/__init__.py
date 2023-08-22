#!/usr/bin/python3
"""creates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   creates a database storage engine (DBStorage).
-> Otherwise, creates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
