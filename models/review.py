#!/usr/bin/python3

""" Review module for the HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text
from os import getenv
from sqlalchemy.orm import relationship


storageType = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'

    if storageType == "db":
        text = Column(Text, nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        # user = relationship("User", back_populates="reviews")
        # place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
