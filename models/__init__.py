#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from os import getenv

Env = getenv('HBNB_TYPE_STORAGE')

if Env == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
