import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
# ... import other model classes ...

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
