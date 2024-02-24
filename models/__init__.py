#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
env_stroage = os.getenv('HBNB_TYPE_STORAGE')
if env_stroage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

if __name__ != "__main__":
    from models.state import State
    from models.city import City
    from models.user import User
    from models.place import Place
    from models.review import Review
    from models.amenity import Amenity
