#!/usr/bin/python3
"""
Define the ``Review`` class that inherits from the class ``BaseModel``
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Define the class Review
    """

    place_id = str()     # it will be Place.id
    user_id = str()     # it will be User.id
    text = str()
