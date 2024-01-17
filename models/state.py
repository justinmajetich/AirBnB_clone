#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.storage == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("Place", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes city"""
        super().__init__(*args, **kwargs)

    if models.storage != "db":
        @property
        def cities(self):
            """getter for city instances related to state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.value():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

