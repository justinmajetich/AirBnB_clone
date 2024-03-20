#!/usr/bin/python3
"""Instantiate the appropriate storage instance for the application"""

# Import necessary modules and classes
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

# Check the value of the environment variable HBNB_TYPE_STORAGE
# If it's set to "db", instantiate a DBStorage instance
# Otherwise, instantiate a FileStorage instance
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage to load data from the chosen storage type
storage.reload()
