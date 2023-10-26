#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base
import os


class State(BaseModel, Base):
    """This is State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """getter attribute cities that returns
            the list of City instances with state_id equals to
            the current State.id => It will be the FileStorage
            relationship between State and City
            """
            import models
            listOfCities = []
            for v in models.storage.all(City).values():
                if v.state_id == self.id:
                    listOfCities.append(v)
            return listOfCities
