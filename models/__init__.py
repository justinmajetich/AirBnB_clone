#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from os import getenv


classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
