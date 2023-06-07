#!/usr/bin/python3
"""
Define the ``State`` class that inherits from the class ``BaseModel``
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Define the class State
    """

    name = str()
