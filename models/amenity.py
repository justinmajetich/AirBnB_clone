#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from re import X
from models.base_model import BaseModel
import os
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """
    creates the tables of amenities
    """
    __tablename__ = "amenities"
    name = Column(128), nullable = False
    #ideas
    #age = Column(Integer, default=1)
    #gender = Column(String(30), default='female')
    #name = ""
    #def __init__(self, *args, **kwargs):
    #super().__init__(*args, **kwargs)
=======
from os import getenv
from models.base_model import BaseModel, Base
# import models
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Class for ammenities """

    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""
>>>>>>> 5677eb38e46ef8c3d150ef66ae3d202454eb152f
