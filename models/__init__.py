#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    dbinst = DBStorage()
    storage = dbinst
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    fileinst = FileStorage()
    storage = fileinst
    storage.reload()
