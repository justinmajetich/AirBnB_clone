#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all,delete', backref='states')
    @property
    def cities(self):
        """ Returns the list of city instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
        """
        from models import storage
        related_cities = []

        cities = storage.all(City) #gets the entire storage a dictionary
        for city in cities.value(): # cities.value returns list of the city objects
            if city.state_id == self.id: # if the object.state.id ==self.id
                related_cities.append(city)
        return related_cities
