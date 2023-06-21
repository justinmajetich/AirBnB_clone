#!/usr/bin/python3
"""
Este módulo crea una instancia de un objeto de clase FileStorage
"""
# from models.base_model import BaseModel, Base
from os import getenv


is_type = getenv("HBNB_TYPE_STORAGE")

if is_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
