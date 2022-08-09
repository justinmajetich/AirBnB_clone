#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import *
from os import getenv

metaData = Base.metadata

place_amenity = Table('place_amenity', metaData,
                      Column('place_id', String(60),\
                             ForeignKey('places.id'), primary_key=True,\
                             nullable=False),
                      Column('amenity.id', String(60),\
                             ForeignKey('amenities.id'), primary_key=True,\
                             nullable=False))

metaData = Base.metadata

place_amenity = Table('place_amenity', metaData,
                      Column('place_id', String(60),\
                             ForeignKey('places.id'), primary_key=True,\
                             nullable=False),
                      Column('amenity_id', String(60),\
                             ForeignKey('amenities.id'), primary_key=True,\
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",\
                               cascade="all, delete, delete-orphan")
    else:
        @property
        def reviews(self):
            """getter return the list of review instances"""
            review_list = []
            for instance in models.storage.all(Review).values():
                if instance.place_id == self.id:
                    review_list.append(instance)
            return review_list


    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity",\
                                 viewonly=False)
    else:
        @property
        def amenities(self):
            """ getter returns the list of amenity instances """
            amenities_list = []
            for instance in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(instance)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """ setter returns appended list """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
            else:
                pass
                

    @amenities.setter
    def amenities(self, value):
        """ setter returns appended list """
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
        else:
            pass
