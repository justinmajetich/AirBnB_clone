#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from uuid import uuid4
from os import environ


s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Amenity(BaseModel, Base):
        """
        This is amenity class
        """
        __tablename__ = 'amenities'
        id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
        name = Column(String(128), nullable=False)
        
        def __init__(self, **kwargs):
            setattr(self, 'id', str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)

else:
    class Amenity(BaseModel):

        name = ""
