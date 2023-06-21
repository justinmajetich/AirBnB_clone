#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """returns the list of City instances with state_id == State.id"""
        list_city = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                list_city.append(city)
        return list_city
