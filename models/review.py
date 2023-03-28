#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """ Set up an instance with its properties. """
        super().__init__(*args, **kwargs)
