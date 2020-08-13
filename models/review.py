#!/usr/bin/python3
""" Review module for the HBNB project """
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
