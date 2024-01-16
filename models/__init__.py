#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

""" Use environment variable to determine storage type"""
storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')

""" Create storage instance based on the value of HBNB_TYPE_STORAGE"""
if storage_type == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
