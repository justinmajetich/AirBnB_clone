#!/usr/bin/python3
"""The module instantiates db storage"""
import os


storage_type = os.getenv('HBNB_TYPE_STORAGE')


if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
