#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
=======
from models.engine.file_storage import FileStorage
from models.engine.db_storage  import DBStorage
>>>>>>> master
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStorage
    storage =  DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD
storage.reload()
=======
    storage.reload()
>>>>>>> master
