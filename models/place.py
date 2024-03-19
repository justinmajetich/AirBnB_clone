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

    def __init__(self, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            if hasattr(self, key) and key != '__class__':
                attr_type = type(getattr(self, key))
                # Convert value to the appropriate type
                if attr_type == int:
                    value = int(value)
                elif attr_type == float:
                    value = float(value)
                setattr(self, key, value)