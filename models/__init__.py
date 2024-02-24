#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')
#Changing the enviromental variable acts as a switch to change storage methods
if type_storage == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
