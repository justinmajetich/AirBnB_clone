#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table

if models.is_db == "db":
    relationship_table = Table('place_amenity', Base.metadata,
                               Column('place_id', String(60),
                                      ForeignKey('places.id'),
                                      primary_key=True),
                               Column('amenity_id', String(60),
                                      ForeignKey('amenities.id'),
                                      primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity',
                             secondary='place_amenity',
                             viewonly=False)
    amenity_ids = []

    if models.is_db != 'db':
        @property
        def reviews(self):
            """ List of reviews related to a place """
            revs = models.storage.all(Review).values()
            return {r for r in revs if r.place_id == self.id}

        @property
        def amenities(self):
            """ List of amenities of a place """
            objs = models.storage.all(Amenity).values()
            return [obj for obj in objs if obj.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """ Amenities setter """
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)