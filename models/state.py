#!/usr/bin/python3
""" State Module for HBNB project """
from models import which_storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if which_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """return list of city instances with state_id equal to
            current instances of state.id
            """
            from models import storage  # Import the storage instance

            my_cities = []
            city_instances = storage.all(City)

            for city in city_instances.values():
                if city.state_id == self.id:
                    my_cities.append(city)
            return my_cities
