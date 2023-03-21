#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from dotenv import load_dotenv
import os


load_dotenv()
storage = FileStorage()
storage.reload()

storage_type = os.getenv('HBNB_TYPE_STORAGE')
if storage_type == db:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
