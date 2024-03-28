#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state",
                          passive_deletes=True)


@property
def cities(self):
    """Returns the cities in this State"""
    Citylist = []
    for city in FileStorage.all(City):
        if city.state_id == self.id:
            Citylist.append(city)
    return Citylist
