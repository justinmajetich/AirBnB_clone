#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

if gentenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
storage.reload()
