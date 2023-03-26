#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base



from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = []

    @property
    def cities(self):
        """ fetch cities from storage """
        cts = storage.all(City)
        objs = []
        for k, v in cts.items():
            if self.id == v.state_id:
                objs.append(v)
        return objs

    cities = relationship("City", back_populates='state',
                          cascade="all, delete, delete-orphan")
