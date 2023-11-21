#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            nullable=False),
        Column('amenity_id', String(60),
            ForeignKey('amenities.id'), nullable=False))
s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Place(BaseModel, Base):
        """
        This is a class for Place
        Attributes:
            city_id: city id
            user_id: user id
            name: name input
            description: string of description
            number_bathrooms: number of bathrooms
            max_guest: maximum number of guest
            price_by_night: price for staying at night
            latitute: latitude in float
            longitude: longitude in float
            amenity_id: list of amenity id
        """
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default= 0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)

        def __init__(self, **kwargs):
            setattr(self, 'id', str(uuid()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class Place(BaseModel):
        """ A place to stay """

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
            all_reviews = models.storage.all(Review)
            liste = []
            keys = all_review.items()
            for k, v in keys:
                if "Review" == k[0:4] and v.places_id == self.id:
                    liste.append(v)
            return(liste)
