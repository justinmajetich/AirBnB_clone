#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
    valid_attr = ['place_id', 'user_id', 'text']

    def __init__(self, *args, **kwargs):
        super(Review, self).__init__()
        for key in self.valid_attr:
            if key in kwargs:
                setattr(self, key, kwargs[key])
