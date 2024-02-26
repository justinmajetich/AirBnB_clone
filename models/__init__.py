#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storage_switch = os.environ.get('HBNB_TYPE_STORAGE')

if storage_switch == 'db':
    storage = DBStorage()
    storage.reload()
elif storage_switch == 'file':
    storage = FileStorage()
    storage.reload() 
