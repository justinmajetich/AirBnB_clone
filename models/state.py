#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import type_of_storage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            cascade='all, delete-orphan',
            backref="state")
    else:
        name = ''

        @property
        def cities(self):
            """
            Returns the list of City instances with state_id
            equal to the current State.id. This is the FileStorage
            relationship between State and City.
            """

            from models import storage

            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
