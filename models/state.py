#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')

    def cities(self):
        """
        returns the list of City instances with state_id equals to the current State.id
        """
        from city import City
        from models import storage
        every_city = storage.all(City)
        cities_list = []
        
        for key, val in every_city.items():
            if val.state_id == self.id:
                cities_list.append(val)

        return cities_list
