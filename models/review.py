#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    from sqlalchemy import String, Column, ForeignKey
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=ForeignKey)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
