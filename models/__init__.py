#!/usr/bin/python3
"""BACKUP VERSIOON"""


from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    storage_engine = DBStorage()
else:
    storage_engine = FileStorage()

storage_engine.reload()
