#!/usr/bin/python3
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
=======
>>>>>>> f130fcd35520c96a54d594ea8d33bc4debf940dd
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
        
