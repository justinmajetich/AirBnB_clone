#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review",
                               cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            reviews_list = []
            reviews_dict = models.storage.all(Review)
            for rev_id, obj in reviews_dict.items():
                if self.id == obj.place_id:
                    reviews_list.append(obj)
            return reviews_list

        @property
        def amenities(self):
            amenity_instances = []
            amenities = models.storage.all(Amenity)
            for key, value in amenities.items():
                if value.id in self.amenity_ids:
                    amenity_instances.append(value)
            return amenity_instances

        @amenities.setter
        def amenities(self, obj):
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
