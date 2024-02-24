#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage
   based on the value of the environment variable HBNB_TYPE_STORAGE.
"""
import os
from models.engine.file_storage import FileStorage

if os.getenv('HBNB_TYPE_STORAGE') != 'db':
    storage = FileStorage()
    storage.reload()
