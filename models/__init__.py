#!/usr/bin/python3
"""BACKUP VERSIOON"""


from models.engine.file_storage import FileStorage
import os

storage = os.getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
