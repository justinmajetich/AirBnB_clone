#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

    @property
    def cities(self):
        """Returns the list of City instances with state_id equals to the current State.id."""
        from models.city import City
        from models import storage
        list_city = list(storage.all(City).values())
        return [city for city in list_city if city.state_id == self.id]
