#!/usr/bin/python3
""" Amenity Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Represent a the Amenities for a place
    
    Inherits the BaseModel and Base(from sqlalchemy) and links to the mysql table amenities
    Attributes:
      __tablename__(str): name of the MySQL table
      name(sqlalchemy String): name of the City
    """
    if models.storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
#        place_amenities = relationship("Place", secondary="place_amenity",
#                                       viewonly=False)
    else:
        def __init__(self, name = ""):
            """ if storage is not db (i.e. FileStorage) instantiate the values """
            self.name = name
            super().__init__()
