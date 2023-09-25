#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import environ

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
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

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", backref="place_amenities",
                                 secondary=place_amenity, viewonly=False)

    else:
        @ property
        def reviews(self):
            """ getter method for reviews"""
            reviews_list = []
            reviews = models.storage.all(Reviews)
            for review in reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @ property
        def amenities(self):
            """ getter method for amenities"""
            amenities_list = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @ amenities.setter
        def amenities(self, object=None):
            """ setter method for amenities"""
            if type(object).__name__ == "Amenity":
                self.amenity_ids.append(object)
