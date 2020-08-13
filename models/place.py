#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':

    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False)
        )


class Place(BaseModel, Base):
    """ place representation """
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        __tablename__ = 'places'
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
        amenities = relationship(
            "Amenity",
            secondary='place_amenity',
            back_populates='place_amenities',
            viewonly=False
            )
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete-orphan'
        )
    else:
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
        def amenities(self):
            """ getter to amenities asociated with the current state """
            from models import storage
            amenities = []
            objects = storage.all("Amenity")
            for obj in objects.values():
                if obj.id == self.amenity_ids:
                    amenities.append(obj)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """ setter to amenities asociated with the current state """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """ getter to reviews asociated with the current place """
            from models import storage
            reviews = []
            objects = storage.all("Review")
            for obj in objects.values():
                if Review == type(obj) and obj.place_id == self.id:
                    reviews.append(obj)
            return obj
