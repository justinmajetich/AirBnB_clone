#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
from models import storage
from models.review import Review
from models.amenity import Amenity
import sqlalchemy

place_amenity = Table('association', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False, primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'states'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review",
                               backref="place", cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        @property
        def reviews(self):
            """getter that returns list of Review instances"""
            objects = storage.all(Review)
            my_list = []
            for value in objects.values():
                if self.id == value.place_id:
                    my_list.append(value)
            return(my_list)

        @property
        def amenities(self):
            """getter that returns list of Amenity instances"""
            objects = storage.all(Amenity)
            my_list = []
            for value in objects.values():
                if self.id == value.place_id:
                    my_list.append(value)
            return(my_list)

        @amenities.setter
        def amenities(self, obj):
            """setter that handles append method for Amenity.id"""
            if isinstance(obj, Amenity):
                self.append(obj)
