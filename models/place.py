#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv


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
    """ Place class """
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

    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        reviews = relationship('Review',
                               cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """ getter for reviews """
            from models import storage
            rev_list = []
            for review in storage.all(Review).values():
                if review.getattr('place_id') == self.id:
                    rev_list.append(review)
            return rev_list

        @property
        def amenities(self):
            """getter for amenities"""
            from models import storage
            amn_list = []
            for amenity in storage.all(Amenity).value():
                if self.id == amenity.place_id:
                    amn_list.append(amenity)
            return amn_list

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            """setter for amenities"""
            if isinstance(obj, Amenity):
                self.append(obj)
