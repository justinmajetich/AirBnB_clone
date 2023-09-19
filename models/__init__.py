#!/usr/bin/python4
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_type = os.getenv('HBNB_TYPE_STORAGE')


if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
