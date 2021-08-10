#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


origin_data = os.getenv("HBNB_TYPE_STORAGE")
if origin_data == "db":
    engine_store = DBStorage()
else:
    engine_store = FileStorage()
engine_store.reload()
