#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represent a review.
    Attributes:
         __tablename__ (str): Name of the table
         place_id (str): The Place id.
         user_id (str): The User id.
         text (str): The text of the review.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')
