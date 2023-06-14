#!/usr/bin/python3
"""
Define the ``User`` class that inherits from the class ``BaseModel``
and 'Base'
"""

from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import (
        Column,
        String,
        relationship
        )


class User(BaseModel, Base):
    """
    Define the class User

    * __tablename__: represents tha table name, 'users'
    * email (String): represents a column containing a string (128 characters)
        * can't be null
    * password (String): represents a column containing a string
        (128 characters)
        * can't be null
    * first_name (String): represents a column containing a string
        (128 characters)
        * can be null
    * last_name (String): represents a column containing a string
        (128 characters)
        * can be null

    # Relationship:
    * places : refers to all the places owned by the user
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationships
    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")
