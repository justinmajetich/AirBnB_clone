#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ
from dotenv import load_dotenv

load_dotenv()

if environ['HBNB_TYPE_STORAGE'] == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
