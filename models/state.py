#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv
class State(BaseModel, Base):
    """State class."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    storage_type = getenv('HBNB_TYPE_STORAGE')
    if storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
