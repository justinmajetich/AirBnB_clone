#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

if models.storage_type == 'db':
    place_amenity = Table('place_amenity',
                          Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 nullable=False,
                                 primary_key=True),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False,
                                 primary_key=True)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
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
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)
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
            '''Retrieves all reviews related to the current place'''
            all_reviews = models.storage.all('Review').values()
            return [review for review in all_reviews
                    if review.place_id == self.id]

        @property
        def amenities(self):
            '''Retrieves all amenities related to the current place'''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            '''Add or update an amenity for the current place'''
            if obj is not None and obj.__class__.__name__ == 'Amenity' and\
                    obj.get('id', None) is not None:
                self.amenity_ids.append(obj.id)
