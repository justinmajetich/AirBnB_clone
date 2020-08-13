#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref='state')

    @property
    def cities(self):
        """
        Returns the cities
        """

        new_dict = models.storage.all(City)
        new_list = []
        for key, value in new_dict.items():
            if value.state_id == self.id:
                new_list.append(value)
        return new_list
