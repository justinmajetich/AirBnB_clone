#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review classto store review information
    Attributes:
    text: description for reviews
    user_id: the user's id
    place_id: place id

    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
