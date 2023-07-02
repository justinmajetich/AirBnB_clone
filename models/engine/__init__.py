"""Update __init__.py: (models/__init__.py)"""

"""hey dipshiut dont forget YOUR IMPORTS EVER AGAIN
DONT FORGET THEM U DUMPPASS!!!!!!!"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
