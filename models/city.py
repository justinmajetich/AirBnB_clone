#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        filtered_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
