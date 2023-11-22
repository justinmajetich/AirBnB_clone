#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel 
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state', cascade='all, delete-orphan');
    base_id = Column(String, ForeignKey('base.id'), nullable=False)

    def cities(self):
        """
        returns the list of City instances with
        state_id equals to the current State.id
        """

        return self.cities
