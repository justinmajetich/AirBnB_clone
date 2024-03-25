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
    amenity_ids = []

    if storage_type == 'db':
        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relationship("Amenity", secondary='place_amenity',
                                backref='place_amenities', viewonly=False)
    else:
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
            all_ame = models.storage.all(Amenity)
            for key, value in all_ame.items():
                if key in self.amenity_ids:
                    amenity_list.append(value)
            return amenity_list

        @amenities.setter
        def amenities(self, value=None):
            """ Setter attribute for amenities """
            if type(value).__name__ == 'Amenity':
                new_ame = 'Amenity' + '.' + value.id
                self.amenity_ids.append(new_ame)
