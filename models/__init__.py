#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

if env['HBNB_TYPE_STORAGE'] == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
