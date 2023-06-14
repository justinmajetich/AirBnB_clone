#!/usr/bin/python3
"""
Define the ``Review`` class that inherits from the class ``BaseModel``
and class 'Base'
"""

from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import (
        Column,
        String,
        ForeignKey
        )


class Review(BaseModel, Base):
    """
    Define the class Review

    * __tablename__: represents the table name, 'reviews'
    * text (String): represents a column containing a string (1024 characters)
        * can’t be null
    * place_id (String): represents a column containing a string \
(60 characters)
        * can’t be null
        * is a foreign key to places.id
    * user_id (String): represents a column containing a string \
(60 characters)
        * can’t be null
        * is a foreign key to users.id
    """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
