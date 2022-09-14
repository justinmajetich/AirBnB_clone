#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay
    Attributes:
    city_id :city id
    -user_id: user id
    -name : customer name
    -description : string value
    -number_rooms: room number in int
    -number_bathrooms :int value
    -max_guest: gust in int
    -price_by_night:int value
    -latitude : latitude in float
    -longitude : longitude in float
    -amenity_ids :list of Amenity ids
   """
