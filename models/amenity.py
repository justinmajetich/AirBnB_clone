#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
# import models
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Class for ammenities """

    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""
