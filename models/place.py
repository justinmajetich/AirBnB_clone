#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    __tablename__ = 'places'
    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=True, default=0)
    number_bathrooms = Column(Integer, nullable=True, default=0)
    max_guest = Column(Integer, nullable=True, default=0)
    price_by_night = Column(Integer, nullable=True, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        """ getter for reviews """
        review_list = []
        for key, value in models.storage.all(Review).items():
            if value.place_id == self.id:
                review_list.append(value)
        return review_list

    @property
    def amenities(self):
        """ getter for amenities """
        amenity_list = []
        for key, value in models.storage.all(Amenity).items():
            if value.place_id == self.id:
                amenity_list.append(value)
        return amenity_list

    @amenities.setter
    def amenities(self, obj):
        """ setter for amenities """
        if type(obj) == Amenity:
            self.amenity_ids.append(obj.id)
