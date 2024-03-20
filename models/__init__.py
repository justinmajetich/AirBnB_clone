#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
