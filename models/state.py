#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """
    State class that inherit from BaseModel
    """
    if models.storageType == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if models.storageType != "db":
        """@property
        def cities(self):
            Getter method that gets a
            list of cities with the same stateid

            allCities = models.storage.all(City)
            citiesList = [city for city in allCities.values()
                        if city.state_id == self.id]
            return citiesList"""
        if getenv("HBNB_TYPE_STORAGE") != "db":
            @property
            def cities(self):
                """Get a list of all related City objects."""
                city_list = []
                for city in list(models.storage.all(City).values()):
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list