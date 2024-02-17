#!/usr/bin/python3

"""
Module initializer for models package.
Instantiates an object of the appropriate storage type based on the value
of the environment variable HBNB_TYPE_STORAGE.
"""

import os
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine import file_storage
from models.engine import db_storage


try:
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        storage = db_storage.DBStorage()
    else:
        raise KeyError
except KeyError:
    storage = file_storage.FileStorage()

storage.reload()
