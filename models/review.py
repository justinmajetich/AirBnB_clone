#!/usr/bin/python3
""" Review module for the BnB v2 project """
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String

from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review class: stores the review information """
    __tablename__ = 'reviews'
    place_id = Column(
        String(60), ForeignKey('places.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
