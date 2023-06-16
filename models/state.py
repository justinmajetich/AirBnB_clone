#!/usr/bin/python3
"""
Define the ``State`` class that inherits from the class ``BaseModel`` \
and ``Base``
"""

from models import storage
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import (
        Column,
        String,
        relationship
        )


class State(BaseModel, Base):
    """
    Define the class State

    * __tablename__: represents the table name, 'cities'
    * name (String): represents a column containing a string (128 characters)
        * can't be null

    # Relationship:
    * cities : represents a list of 'City' objects linked to this
        'State' instance
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # Relationship:
    if isinstance(storage, DBStorage):
        # DBStorage relationsip between 'State' and 'City'
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    elif isinstance(storage, FileStorage):
        # FileStorage relationship between 'State' and 'City'
        @property
        def cities(self):
            """
            Return a list of 'City" instances with state_id equal to
            self.id
            """
            objs = list()
            for obj in storage.all():
                if obj.state_id == self.id:
                    objs.append(obj)

            return objs
