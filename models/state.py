#!/usr/bin/python3

"""
Module for the State class.
"""

import models
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """
    Class representing a state in the application.
    Inherits from BaseModel and Base.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            """
            Getter attribute that returns the list of City instances associated
            with the current state.
            Returns:
                List of City instances associated with the current state.
            """
            all_cities = models.storage.all("City")
            temp = []
            for c_id in all_cities:
                if all_cities[c_id].state_id == self.id:
                    temp.append(all_cities[c_id])

            return temp
