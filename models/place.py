#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                              ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60),
                              ForeignKey('amenities.id'), primary_key=True))
storage_type = getenv('HBNB_TYPE_STORAGE')

class Place(BaseModel, Base):
    """ A place to stay """
    if storage_type == 'db':
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relationship("Amenity", secondary='place_amenity',
                                backref='place_amenities', viewonly=False)
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

        @property
        def reviews(self):
            """ Getter attribute that returns the list of Reviews associated with the Place """
            from models import storage
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """ Getter attribute for the linked amenities """
            amenity_list = []
            all_ame = models.storage.all(Amenity).values()
            for obj in all_ame:
                if 'Amenity' + obj.id in self.amenity_ids:
                    amenity_list.append(obj)
            return amenity_list

        @amenities.setter
        def amenities(self, value=None):
            """ Setter attribute for amenities """
            if isinstance(value, Amenity):
                amenity_id = 'Amenity' + value.id
                if amenity_id not in self.amenity_ids:
                    self.amenity_ids.append(amenity_id)
