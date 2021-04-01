#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref='state', cascade='delete')
    else:
        @property
        def cities(self):
            """ Method that gets cities"""
            cityList = []
            for city in storage.all(City).values():
                if city.getattr('state_id') == self.id:
                    cityList.append(city)
            return(cityList)
