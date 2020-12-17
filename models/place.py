#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.engine import FileStorage


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade="all, delete", backref="place")

    @property
    def reviews(self):
        """ return Reviews """
        lower = []
        for key, value in FileStorage.__objects.items():
            if value.place_id == self.id:
                lower.append(value)
        return lower
