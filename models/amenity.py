#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", backref="amenities")
