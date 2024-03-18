#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


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
