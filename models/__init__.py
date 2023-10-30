#!/usr/bin/python3
"""Checks value of HBNB_TYPE_STORAGE"""
import os
from models.engine.file_storage import FileStorage


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
