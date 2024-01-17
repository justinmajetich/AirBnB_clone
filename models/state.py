#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)

    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    # For FileStorage
    @property
    def cities(self):
        """ Getter attribute cities that returns the list of City instances with state_id equals to the current State.id """
        from models import storage
        cities_list = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

    def __init__(self, *args, **kwargs):
        super().__init__()

        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
