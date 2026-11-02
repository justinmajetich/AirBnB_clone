#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if (getenv("HBNB_TYPE_STORAGE") == 'db'):
        name = Column(String(128), nullable=False)
        # cities = relationship('City')
        cities = relationship('City', cascade="all, delete", backref='state')
    else:
        @property
        def cities(self):
            '''returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            '''
            from models import storage
            related_cities = []

            """
            cities = storage.all(City)
            # gets the entire storage- a dictionary
            for key, value in cities.items():
                # cities.value returns list of the city objects
                if value.state_id == self.id:
                    # if the object.state_id == self.id
                    related_cities.append(value)
                    # append to the cities list
            return related_cities
            """

            '''
            cities = storage.all(City).items()
            # gets the entire storage- a dictionary
            for city in cities.values():
                    # cities.value returns list of the city objects
                if city.state_id == self.id:
                        # if the object.state_id == self.id
                    related_cities.append(city)
                    # append to the cities list
            return related_cities
                # state = relationship('State')
                #the above block of code is buggy because,
                we use the items() on 43
                #which returns a dict with a key and
                value pair but we return just the
                #key and do not return the value of the key
            '''

            # another implementation of lines 43 to 47
            cities = storage.all(City)
            for key in cities.keys():
                if cities[key].state_id == self.id:
                    related_cities.append(cities[key])
            return related_cities
