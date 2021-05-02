#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # creating relationship with cities

    storage_type = os.getenv("HBNB_TYPE_STORAGE")
    if storage_type == "db":
        cities = relationship("City",
                              cascade="all, delete",
                              backref="state")
    else:
        @property
        def cities(self):
            _cities_list = []
            cities_dict = models.storage.all(City)
            for city_id, obj in cities_dict.items():
                if self.id == obj.state_id:
                    _cities_list.append(obj)
            return _cities_list
