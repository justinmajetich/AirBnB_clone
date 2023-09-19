#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        """Returns the list of City instances
        with state_id equals to the current State.id
        """
        import models
        stored = models.storage.all()
        for k, v in stored.items():
            if v[__class__] == 'State':
                return [city for city in self.cities if
                        city.state_id == self.id]
