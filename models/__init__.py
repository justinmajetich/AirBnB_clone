#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

if (os.getenv("HBNB_TYPE_STORAGE") == 'db'):
    from models.engine import db_storage
    storage = db_storage.DBStorage()
    storage.reload()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
