#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary="place_amenity",
                                   viewonly=False
                                  )
