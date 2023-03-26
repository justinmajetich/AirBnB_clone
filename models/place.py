#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    # Condition required for task 9
    # if getenv("HBNB_TYPE_STORAGE") == "db":
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

    # Condition for task 9
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # relation with class-table Reviews
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        user = relationship('User', backref='places')
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     nullable=False, primary_key=True),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     nullable=False, primary_key=True)
                              )

        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        # Condition for task 9
        # if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ getter: return list of reviews"""
            list_reviews = []
            dic_reviews = models.storage.all(Review)
            for review in dic_reviews.values():
                # for review in self.reviews:
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """ getter: return list of amenities """
            list_amenities = []
            dic_amenities = models.storage.all(Amenity)
            for amenity in dic_amenities.values():
                if amenity.id == self.place_amenity.amenity_id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """ setter: append Amenity_id to amenity_ids """
            if isinstance(obj, self.__class__):
                amenity_ids.append(obj.id)
