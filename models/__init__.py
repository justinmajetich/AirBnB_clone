#!/usr/bin/python3
"""This module initialise Storage"""
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = FileStorage()

storage.reload()
