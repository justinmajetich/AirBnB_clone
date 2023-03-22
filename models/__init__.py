#!/usr/bin/python3
"""a conditional depending of the value of the environment 
variable HBNB_TYPE_STORAGE
If equal to db: 
    Import DBStorage class in this file
    Create an instance of DBStorage and store it in the variable storage 
    (the line storage.reload() should be executed after this instantiation
Else:
    Import FileStorage class in this file
    Create an instance of FileStorage and store it in the variable storage 
    (the line storage.reload() should be executed after this instantiation)
"""

from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBstorage
    storage = DBstorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
