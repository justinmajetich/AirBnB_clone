#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

storage = None
stype = os.getenv('HBNB_TYPE_STORAGE')
if stype == 'db':
    from models.engine.db_storage import DBStorage as DBS
    storage = DBS()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
