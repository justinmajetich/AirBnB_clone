#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Column, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


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
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref="places", viewonly=False)
        reviews = relationship('Review', backref='place',
                           cascade='all, delete-orphan')
    @property
    def reviews(self):
        """Get the lists of review"""
        lists_of_review = []
        for revw in models.storage.all(Review).values():
            if revw.place_id == self.id:
                lists_of_review.append(revw)
        return lists_of_review

    @property
    def amenities(self):
        """getter: returns the list of Amenity"""
        lists_of_Amenity = []
        for amnt in models.storage.all(Amenity).values():
            if amnt.amenity_ids == self.id:
                lists_of_Amenity.append(amnt)
        return lists_of_Amenity

    @amenities.setter
    def amenities(self, objct):
        """amenities setter"""
        if type(objct) == 'Amenity':
            self.amenity_ids.append(objct.id)
