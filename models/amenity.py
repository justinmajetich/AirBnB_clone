#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models

if models.env_stroage == 'db':
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.orm import relationship
    from models.place import place_amenity

    class Amenity(BaseModel, Base):
        """
        class amenity
        """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        places = relationship('Place', secondary=place_amenity, viewonly=False)

else:
    class Amenity(BaseModel):
        """
        class amenity
        """
        name = ""
        place_amenities = ""
        place_amenities = []
