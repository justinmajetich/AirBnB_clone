#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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

    reviews = relationship("Review", backref="place")
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False, overlaps="place_amenities")
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        amenity_ids = []

        @property
        def reviews(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            from models.__init__ import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ return list of amenities """
            from models.__init__ import storage
            amenities_list = []
            for obj in storage.all(Amenity).values():
                if obj.id == self.amenity_ids:
                    amenities_list.append(obj)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """ sets the amenities """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
            else:
                pass
