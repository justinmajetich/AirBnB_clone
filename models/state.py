#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """
    State class that inherit from BaseModel
    """
    if models.storageType == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="all, delete")
    else:
        name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    if models.storageType != "db":
        @property
        def cities(self):
            """ Getter method that gets a
            list of cities with the same stateid
            """
            allCities = models.storage.all(City)
            citiesList = [city for city in allCities.values()
                        if city.state_id == self.id]
            return citiesList
