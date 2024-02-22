#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = 'amenities'

    def __init__(self, *args, **kwargs):
        """ Setting up initialization for the Amenity class
            *args: Is not been used
        """
        if getenv("HBNB_TYPE_STORAGE") != "db":
            super().__init__(**kwargs)
            class_attr = ["name"]
            self.name = ""
            if kwargs:
                sub_dict = {k: kwargs[k] for k in class_attr if kwargs.get(k)}
                self.__dict__.update(sub_dict)

    name = Column(String(128), nullable=False)

    place_amenity = relationship("Place", secondary="place_amenity",
                                 back_populates="amenities")
