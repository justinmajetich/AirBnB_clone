#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from . import storage
import uuid


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Review.place_id = kwargs.get('place_id', Review.place_id)
        Review.user_id = kwargs.get('user_id', Review.user_id)
        Review.text = kwargs.get('text', Review.text)
       
