#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    @property
    def cities(self):
        """Returns list of city instances in same state"""
        from models import storage
        my_list = []
        for i in list(storage.all(City).values()):
            if self.id == i.state_id:
                my_list.append(i)
        return my_list
