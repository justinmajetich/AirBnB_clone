#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from environ import get_env

if get_env('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

elif get_env('HBNB_TYPE_STORAGE') == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
