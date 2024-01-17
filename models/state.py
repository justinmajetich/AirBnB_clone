#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        from models import storage
        city_instances = []

        for city in storage.all(City).value():
            if city.state_id == self.id:
                city_instances.append(city)

        return (city_instances)
