#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Amenity(BaseModel, Base):
    """ """
    name = ""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   back_populates="amenities",
                                   cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize Amenity instances
            Args:
                args: list of arguments
            kwargs:
                key/value dictionary of arguments
        """
        super().__init__(args, kwargs)
