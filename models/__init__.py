#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.DB_stoarage  import DBstorage
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
   storage =  DBstorage()
   storage.reload()

else:
    HBNB_TYPE_STORAGE == "FileStorage"
    storage = FileStorage()
    storage.relaod()
