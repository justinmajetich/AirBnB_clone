#!/usr/bin/env python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage


env = os.getenv('HBNB_TYPE_STORAGE')
if env is None or env != 'db':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

storage.reload()
