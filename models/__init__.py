#!/usr/bin/python3
"""This module instantiates a storage object

If the environment variable 'HBNB_TYPE_STORAGE' is set to be 'db',
  instantiates a DB Storage engine (DBStorage)
Else instantiates a File storage engine (FileStorage)
"""

from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
