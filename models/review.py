#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        ''' File Storage relationship '''
        @property
        def cities(self):
            '''
            returns the list of City instances
            with state_id equals to the current State.id
            '''
            from models import storage
            from models.city import City

            city_list = []
            city_dict = storage.all(City)

            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
