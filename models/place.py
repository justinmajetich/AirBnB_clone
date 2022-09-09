#!/usr/bin/python3
""" Place Module for HBNB project """
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref='place', cascade="delete")
    else:
        @property
        def reviews_att(self):
            """Defines review attribute for FileStorage"""
            from models import storage
            cities_dict = storage.all('Review')
            cities_list = []
            for key, value in cities_dict.items():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_list
