#!/usr/bin/python3
""" Place Module for HBNB project """


import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity

class Place(BaseModel, Base):
    """A place to stay"""
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

    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        metadata = Base.metadata
        place_amenity = Table(
            'place_amenity', metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                   primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                   primary_key=True, nullable=False)
        )
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:
        @property
        def amenities(self):
            from models import storage
            amenities_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get("Amenity", amenity_id)
                if amenity:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
