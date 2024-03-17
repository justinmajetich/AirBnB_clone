#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os


hbnb_environ = os.getenv('HBNB_TYPE_STORAGE')
if hbnb_environ == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
