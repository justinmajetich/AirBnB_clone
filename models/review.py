#!/usr/bin/python3
"""Review module for the HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import type_of_storage


class Review(BaseModel, Base):
    """Review class to store review information"""

    __tablename__ = 'reviews'

    if type_of_storage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
