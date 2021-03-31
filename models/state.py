#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    """ if the system have a env var its gonna use de database """

    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            cities_instances = FileStorage.all(City)
            cities_list = []
            for key, value in cities_instances.items():
                if self.id == value.state_id:
                    cities_list.append(value)
            return cities_list
