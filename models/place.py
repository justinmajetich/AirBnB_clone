#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


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
    amenity_ids = []
    reviews = relationship('Review',
                           cascade='all,delete',
                           backref='user')
    amenities = relationship('Amenity',
                             secondary=place_amenity,
                             backref='places',
                             viewonly=False)

    @property
    def reviews(self):
        """reviews getter"""
        return self.reviews

    @property
    def amenities(self):
		"""amenitites getter"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, amenity_ids):
		"""amentities setter"""
        amenities = models.storage.all(Amenity)
        for amenity in amenities.values():
            if amenity.place_id == self.id:
                amenity_ids.append(amenity.id)
