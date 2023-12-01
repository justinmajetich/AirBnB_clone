#!/usr/bin/python3
"""
    This module defines the Place class
    *Update 30/11/2023: added code to use db storage and associated imports
    *Update 1/12/2023: added code to use FileStorage and associated imports
        part of question 10
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

metadata = Base.metadata


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    # user = relationship('User', back_populates='places')
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
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

        @property
        def reviews(self):
            """return list of Review instances where place_id = Place.id"""
            from models import storage
            from models.review import Review
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """
                getter attribute amenities
            """
            from models import storage
            amenities_dict = storage.all("Amenity")
            amenities_list = []
            for key, value in amenities_dict.items():
                if value.id in self.amenity_ids:
                    amenities_list.append(value)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """
                setter attribute amenities
            """
            from models.amenity import Amenity
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)

    else:
        reviews = relationship('Review', backref='place',
                               cascade="delete, delete-orphan")
        cities = relationship('City', back_populates='places')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
