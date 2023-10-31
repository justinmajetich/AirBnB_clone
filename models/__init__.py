#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
