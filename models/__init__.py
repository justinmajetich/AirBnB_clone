#!/usr/bin/python3
""" This module instantiates an object of class
    FileStorage or class DBStorage.
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

# check the origin of the data to select the engine
data_origin = os.getenv("HBNB_TYPE_STORAGE")
# db engine
if data_origin == "db":
    storage = DBStorage()
# file engine
else:
    storage = FileStorage()
# upload the data
storage.reload()
