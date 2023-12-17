#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class for storing state info """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # This for DataBase Storage
    if storage_type == 'db':
        cities = relationship('City', cascade='all, delete-orphan',
                              back_populates='state')

    def __init__(self, *args, **kwargs):
        """ Initialise State instance """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """ Getter attribute for cities (for FileStorage) """
        city_list = []
        for city in models.storage.all(models.Cit)y.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
