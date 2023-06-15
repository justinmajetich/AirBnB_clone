#!/usr/bin/python3
"""
Resources for this package

This module instantiates the type of Storage to use for the project
"""
from os import getenv


# Create a unique storage instance for the application
storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage
storage.reload()

"""
NOTE:
    In this extra imports, A special comment `# noqa: E402` is included.
    This comment tells 'pycodestyle' to ignore ERROR E402.
    This error is raised if import statements are located 'not at the top
    of the file'
"""
# Extra imports
from models.state import State      # noqa: E402
from models.place import Place      # noqa: E402
from models.city import City        # noqa: E402
from models.user import User        # noqa: E402
from models.review import Review    # noqa: E402
from models.amenity import Amenity  # noqa: E402
