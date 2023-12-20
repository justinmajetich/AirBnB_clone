#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    """
    Amenity class
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128),
                      nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity",
            backref='amenities',
            viewonly=False
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes Amenity
        """
        super().__init__(*args, **kwargs)
