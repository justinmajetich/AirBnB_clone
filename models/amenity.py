#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String


class Amenity(BaseModel, Base):
    """
        Represents a user in the database.

        Attributes:
            __tablename__ (string): The name of the amenity table.
            name (sqlalchemy string): The name of the amenity.
            place_amenities (sqlalchemy relationship): The Place-Amenity
                                                       relationship.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
