#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from models.base_model import Base, BaseModel
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base):
    """ Class for Place Module """
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
    else:
        @property
        def reviews(self):
            """ Returns list of Reviews """
            from models import storage
            reviews = storage.all(Review).values()
            return list(filter(lambda review: review.place_id == self.id,
                               reviews))
        amenity_ids = []
