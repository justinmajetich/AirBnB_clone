#!/usr/bin/python3
"""
State Module for HBNB project
"""
from os import getenv
# from sqlalchemy.ext.declarative import de
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import uuid


class State(BaseModel, Base):
    """ The state class, contains name """

    __tablename__ = "states"
    id = Column(String(60), primary_key=True, nullable=False, default=uuid.uuid4().hex)
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """getter attribute that returns the list of City instances"""
            from models.city import City
            cities_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid4().hex
