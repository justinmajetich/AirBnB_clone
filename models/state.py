#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('Cities', backref='state')

    @property
    def cities(self):
        """List of City instances with id of state"""
        from models import storage
        new = []
        for key, obje in storage.all(City).items():
            if obje.state_id == self.id:
                new.append(obje)
        return new
