#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage



if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()

storage.reload()