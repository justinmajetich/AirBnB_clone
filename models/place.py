#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class Place(BaseModel, Base):
    """ A place to stay """
    from sqlalchemy import Column, String, ForeignKey, Integer, Float

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128),  nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Place.city_id = kwargs.get('city_id', Place.city_id)
        Place.user_id = kwargs.get('user_id', Place.user_id)
        Place.name = kwargs.get('name', Place.name)
        Place.description = kwargs.get('description', Place.description)
        Place.number_rooms = kwargs.get('number_rooms', Place.number_rooms)
        Place.number_bathrooms = kwargs.get('number_bathrooms',
                                            Place.number_bathrooms)
        Place.max_guest = kwargs.get('max_guest', Place.max_guest)
        Place.price_by_night = kwargs.get('price_by_night',
                                          Place.price_by_night)
        Place.latitude = kwargs.get('latitude', Place.latitude)
        Place.longitude = kwargs.get('longitude', Place.longitude)
        Place.amenity_ids = kwargs.get('amenity_ids', Place.amenity_ids)
