#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.dbstorage == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all,delete', backref='state')
    else:
        name = ""

    if models.dbstorage != "db":
        @property
        def cities(self):
            """ Returns the list of city instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            """
            related_cities = []
            cities = models.storage.all(City)
            """gets the entire storage a dictionary"""
            for city in cities.values():
                """cities.value returns list of the city objects"""
                if city.state_id == State.id:
                    """if the object.state.id == self.id"""
                    related_cities.append(city)
            return related_cities
