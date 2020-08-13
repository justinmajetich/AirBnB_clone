#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base, Table, Column, String
from sqlalchemy import ForeignKey
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """
        initialize from the BaseModel class
        """
        super().__init__(*args, **kwargs)
