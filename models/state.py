#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    
    @property
    def cities(self):
        """
        Returns the list of `City` instances 
        where `state_id` equals to the current
        """

        cities = list()

        for _id, city in models.storage.all(City).items():
            if city.state_id == self.id:
                cities.append(city)

        return cities
