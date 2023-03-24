#!/usr/bin/python3

from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.dbstorage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.filestorage import Filestorage
    storage = Filestorage()
    storage.reload()
