#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # Database storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")

    # File storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """
            Getter attribute cities that returns the list of
            City instances with state_id equals to the
            current State.id
            """
            obj_cities = models.storage.all(City).values()
            return [c for c in obj_cities if self.id == c.state_id]
