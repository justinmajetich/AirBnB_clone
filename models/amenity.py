#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.place import place_amenity
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

st = getenv("HBNB_TYPE_STORAGE")

class Amenity(BaseModel, Base):

    __tablename__ = "amenities"
    if st == "db":
        name = Column(String(128),
                nullable=False)

        place_amenities = relationship(
                "Place",
                secondary=place_amenity,
                viewonly=False,
                back_populates="amenities")
    else:
        name = ""
