#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4

s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class City(BaseModel, Base):
        '''
        This is the class for City Attributes
        '''
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all,delete")

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)
else:
    class City(BaseModel):
        '''
        This is the class for City
        '''
        state_id = ""
        name = ""
