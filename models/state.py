#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel):
    """ State class """


    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all")

    else:
        name = ""

        @property
        def cities(self):
            """ Getter for cities """
            city_all = models.storage.all(models.City)
            return [city for city in city_all.values() if city.state_id == self.id]
