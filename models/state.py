#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128),
        nullable =False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City
            """
            result = []
            for a, i in models.storage.all(models.city.City).items():
                if (i.state_id == self.id):
                    result.append(i)
            return result