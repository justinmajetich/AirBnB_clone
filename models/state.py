#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """ getter of all cities under a state
            return:
                list of cities in that state
        """
        all_obj = storage.all()
        city_list = []
        cities = []
        for key in all_obj:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                city_list.append(all_obj[key])
        for elem in city_list:
            if (elem.state_id == self.id):
                cities.append(elem)
        return (cities)
