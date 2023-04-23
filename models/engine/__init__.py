#!/usr/bin/python3
""" This module creates an object of class storage """

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
