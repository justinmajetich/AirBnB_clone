#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.city import City
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
