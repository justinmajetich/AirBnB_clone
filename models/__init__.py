#!/usr/bin/python3
"""
Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
    instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
