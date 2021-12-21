#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                if hasattr(self, key) and key != '__class__':
                    setattr(self, key, kwargs[key])
