#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    place_amenity = Table('place_amenity',Base.metadata,
                          column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """
    __tablename__= 'places'
    city_id = column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = column(String(60), ForeignKey('user_id'), nullable=False)
    name = column(String(128), nullable=False)
    description = column(String(1024), nullable=True)
    number_rooms = column(Integer, default=0, nullable=False)
    number_bathrooms = column(Integer, default=0, nullable=False)
    max_guest = column(Integer, default=0, nullable=False)
    price_by_night = column(Integer, default=0, nullable=False)
    latitude = column(float, nullable=True)
    longitude = column(Integer, default=0, nullable=True)
else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """getter attribute reviews that
        returns the list of Review instances
        with place_id equals to the current Place.id"""
        from models import storage
        from models.review import Review
        reviews = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews.append(review)
        return reviews

    @property
    def amenities(self):
        """getter attribute amenities that returns the list of Amenity
        instances based on the attribute amenity_ids that contains all
        Amenity.id linked to the Place"""
        from models import storage
        from models.amenity import Amenity
        amenities = []
        for amenity in storage.all(Amenity).values():
            if amenity.id in self.amenity_ids:
                amenities.append(amenity)
        return amenities
