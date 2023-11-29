#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
=======
from models.base_model import BaseModel
"""
Module class: City
"""


class City(BaseModel):
    """definition for class City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
>>>>>>> master
