#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

st = getenv("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = "reviews"
    if st == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"),nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"),nullable=False)

        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
