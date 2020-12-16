#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import state
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = states
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @propety
    def cities(self):
        """ Retur Cities """
        List = []
        Allcities = models.storage.all(city)
        for city in Allcities.values():
            if city.state_id == self.id:
                List.append(city)
        return List
