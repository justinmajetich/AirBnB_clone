#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4


s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    """
    This is a class for city attributes
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")

    def __init__(self, **kwargs):
        setattr(self, 'id', str(uuid4()))
        for k, v in kwargs.items():
            setattr(self, k, v)

else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
