#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
"""
assign value HBNB_TYPE_STORAGE to type_storage
"""
type_storage = getenv(HBNB_TYPE_STORAGE)
"""
assign storage based on HBNB_TYPE_STORAGE
"""
if type_storage == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
