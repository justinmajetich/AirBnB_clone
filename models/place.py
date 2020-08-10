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
    valid_attr = ['city_id', 'user_id', 'name', 'description',
                  'number_rooms', 'number_bathrooms', 'max_guest',
                  'price_by_night', 'latitude', 'longitude', 'amenity_ids']

    def __init__(self, *args, **kwargs):
        super(Place, self).__init__()
        for key in self.valid_attr:
            if key in kwargs:
                setattr(self, key, kwargs[key])
