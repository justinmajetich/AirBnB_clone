#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

Env = getenv('HBNB_TYPE_STORAGE')

if Env == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
