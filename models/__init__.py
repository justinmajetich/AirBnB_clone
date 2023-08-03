#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State
from .user import User

env_db = getenv("HBNB_TYPE_STORAGE")

if env_db == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
