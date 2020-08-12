#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Integer
from models.cities import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(length=128), nullable=False)
    id = Column(Integer(), primary_key=True)

    @property
    def cities(self, states):
        """ getter to cities asociated with the current state """
        cities = []
        objects = storage._FileStorage__objects
        for obj in objects.values():
            if City == type(obj) and obj.state_id = self.id:
                cities.append(obj)
        return obj
