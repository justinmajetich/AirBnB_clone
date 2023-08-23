#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Place Class
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: description of the place
        number_rooms: number of romm
        number_bathrooms: number of bathrooms
        max_guest: maximum guest
        price_by_night: price by night
        latitude: latitude
        longitude: longitude
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """Return the list of Review instances with
            place_id == current Place_id
            """
            objects = models.storage.all()
            lis = []
            res = []
            for k in objects:
                rev = k.replace('.', ' ')
                rev = shlex.split(review)
                if (rev[0] == 'Review'):
                    lis.append(objects[k])
            for rev in lis:
                if (rev.place_id == self.id):
                    res.append(rev)
            return (res)

        @property
        def amenities(self):
            """Returns lists of amenities"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """set amenities_ids"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenities_ids.append(obj.id)
