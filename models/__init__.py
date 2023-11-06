#!/usr/bin/python3
# KASPER edited @ 10/30 11:40pm
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


enviornment = getenv("HBNB_TYPE_STORAGE")

if enviornment == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
