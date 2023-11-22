#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    attributes:
        name: empty
    """
    name = ""

    def __init__(self, *args, **kwargs):
        filtered_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
