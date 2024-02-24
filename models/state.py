#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models

if models.env_stroage == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade="all, delete-orphan")

else:
    class State(BaseModel):
        """ State class for State """
        name = ''

        @property
        def cities(self):
            from models import storage
            allcit = storage.all(City).values()
            return [city for city in allcit if hasattr(city, 'state_id') and
                    city.state_id == self.id]
