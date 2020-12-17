#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.city import City
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
storage_type = getenv('HBNB_TYPE_STORAGE')


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Define Place class and implement of relationships"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete",
                           backref="place")
    amenities = relationship('Amenity', secondary=place_amenity,
                             backref='places', viewonly=False)


if getenv('HBNB_TYPE_STORAGE') != "db":
    @property
    def reviews(self):
        """class property getter for reviews associated to Place """
        list_reviews = []
        __objects = models.storage.all(Review)
        for k, obj in __objects.items():
            if place_id in obj and obj.place_id == self.id:
                list_reviews += obj
        return list_reviews

    @property
    def amenities(self):
        """A getter for amenities"""
        return self.__amenity_ids

    @amenities.setter
    def amenities(self, amenity_ids):
        """A setter for amenities"""
        amenity_list = []
        amenities = models.storage.all(Amenity)
        for amenity in amenities.values():
            if amenity.place_id == self.id:
                amenity_ids.append(amenity.id)
