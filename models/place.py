#!/usr/bin/python3
"""
Define the ``Place`` class that inherits from the class ``BaseModel``
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Define the class Place
    """

    city_id = str()     # City.id
    user_id = str()     # User.id
    name = str()
    description = str()
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = list(str())   # list of Amenity.id
