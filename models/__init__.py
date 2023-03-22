#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
