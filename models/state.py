#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from file_storage import FileStorage
from city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')
    # for FileStorage: getter attribute cities that returns the list of
    # City instances with state_id equals to the current State.id => It
    # will be the FileStorage relationship between State and City

    def cities(self):
        """Retrieve cities with state_id 
           equals to the current State.id"""
        return FileStorage.get_instances_by_attribute(City, 'state_id',
                                                      self.id)
