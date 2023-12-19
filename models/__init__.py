#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage



if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
