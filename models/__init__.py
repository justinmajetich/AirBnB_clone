#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
=======
"""
This module creates an instance of a FileStorage class object.
"""
# from models.base_model import BaseModel, Base
from os import getenv


is_type = getenv("HBNB_TYPE_STORAGE")

if is_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

>>>>>>> 3723cb901fd626ce8041c3c37f8d6f09336c73a5
storage.reload()
