#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

dbStorage = getenv('HBNB_TYPE_STORAGE')
if (dbStorage == 'db'):
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
