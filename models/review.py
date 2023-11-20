#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4


s = "HBNB_TYPE_STORAGE"
if s inenviron.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Review(BaseModel, Base):
        """
        This is a class for Review
        Attribute:
            Place_id: place id
            user_id: user id
            text: review description
        """
        __tablename__ = "reviews"
        text = Column(String(128), nillable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, 'id', str(uuid4()))
            for k, v in kwargs.values():
                setattr(self, k, v)
else:
    class Review(BaseModel):
        """ Review classto store review information """
        place_id = ""
        user_id = ""
        text = ""
