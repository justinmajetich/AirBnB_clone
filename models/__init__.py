#!/usr/bin/python3
'''Package initializer'''

from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os


classes = {"User": User, "BaseModel": BaseModel, "Place": Place,
           "State": State, "City": City, "Amenity": Amenity, "Review": Review}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
