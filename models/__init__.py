#!/usr/bin/python3
"""Creates a unique FileStorage instance for this application."""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

__all__ = ["amenity", "city", "place", "state",
           "base_model", "review", "user", "engine"]

storage = DBStorage() if os.getenv('HBNB_TYPE_STORAGE') == 'db' else FileStorage()
storage.reload()
