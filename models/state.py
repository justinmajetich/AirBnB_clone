#!/usr/bin/python3
""" 0x02. AirBnB clone - MySQL, task 6. DBStorage - States and Cities """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .base_model import Base
from . import storage


class State(BaseModel):
    """Defines attributes for `State` as it inherits from `BaseModel`,
    and ORM properties in relation to table `states`.

    Attributes:
        name (Column): name of state, string of max 128 chars
        cities (relationship): one-to-many-association to `City`
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """ Getter for `cities` when in file storage mode. """
        cities = []
        for obj in storage._FileStorage__objects.values():
            if obj.__class__.__name__ == 'City':
                if obj.state_id == self.id:
                    cities.append(obj)
        return cities
