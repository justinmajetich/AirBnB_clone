#!/usr/bin/python3

"""
Module for the City class, representing a city in the application.
"""

from models import *
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    Class representing a city in the application.
    Inherits from BaseModel and Base.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
