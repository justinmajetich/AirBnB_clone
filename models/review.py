#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        place_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)

            def __init__(self, **kwargs):
            self.id = str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)

    else:
        place_id = ''
        user_id = ''
        text = ''
