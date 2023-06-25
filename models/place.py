#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy import Table, Column, Integer
from sqlalchemy import Float, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from models.base_model import BaseModel, Base
from os import environ

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """
            Returns the list of Review instances
            with place_id equals to the current Place.id
            """
            all_reviews = models.storage.all(Review)
            place_reviews = []
            for review_ins in all_reviews.values():
                if review_ins.place_id == self.id:
                    place_reviews.append(review_ins)

            return place_reviews

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id
            linked to the Place
            """
            all_amenities = models.storage.all(Amenity)
            place_amenities = []
            for amenity_ins in all_amenities.values():
                if amenity_ins.place_id == self.id:
                    place_amenities.append(amenity_ins)

            return place_amenities

        @amenities.setter
        def amenities(self, amenity_obj):
            """
            Handles append method for adding an Amenity.id to the attribute
            amenity_ids
            """
            if isinstance(amenity_obj, models.Amenity):
                self.amenities.append(amenity_obj.id)
