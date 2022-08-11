#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), nullable=False)
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), nullable=False))

    class Place(BaseModel, Base):
        """ The Place class, contains city_id, user_id, name,
        description, number_rooms, number_bathrooms, max_guest,
        price_by_night, latitude and longitude """

        __tablename__ = 'places'
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
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)
else:
    class Place(BaseModel):
        """This class defines a place by various attributes"""
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
            """ Returns the list of Review instances
            with `state_id` equals to the current id
            """
            reviews = []
            for value in models.storage.all(Review).values():
                if value.place_id == self.id:
                    reviews.append(value)
            return reviews

        @property
        def amenities(self):
            """ Getter attribute in case of file storage """
            amenities = []
            for value in models.storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities.append(value)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """ Adding an Amenity.id to the amenity_ids """

            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
