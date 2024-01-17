#!/usr/bin/python3
""" Place Module for HBNB project """
import uuid
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
        """ Initializes a new Place instance """
        super().__init__(*args, **kwargs)
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())
