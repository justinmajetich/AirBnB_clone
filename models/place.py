#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'),
                              primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities.id'),
                              primary_key=True, nullable=False))
    __tablename__ = 'places'
    if getenv("HBNB_TYPE_STORAGE") == "db":
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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            viewonly=False, backref="places")
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
            """reviews getter"""
            from models import storage
            result = []
            dict_reviews = storage.all(Review)
            for key, obj in dict_reviews.items():
                if self.id == obj["place_id"]:
                    result.append(obj)
            return result

        @property
        def amenities(self):
            """amenities getter"""
            from models import storage
            from models.amenity import Amenity
            result = []
            for key, obj in storage.all(Amenity).items():
                if key.id == self.amenity_ids:
                    result.append(obj)
            return result

        @amenities.setter
        def amenities(self, value):
            """Amenities setter"""
            from models import storage
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
