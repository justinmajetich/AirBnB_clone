#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equals to the current State.id (FileStorage)
            """
            from models import storage
            cities_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
