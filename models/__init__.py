#!/usr/bin/python3
"""
module executes whn models package is imported
"""


from models.engine.file_storage import FileStorage
<<<<<<< HEAD
from os import getenv
from models.engine.db_storage import DBStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()

else:
    storage = FileStorage()
    storage.reload()
=======
storage = FileStorage()
storage.reload()
>>>>>>> master
