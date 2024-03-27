#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DBStorage
    if os.environ.get('HBNB_MYSQL_DB') == 'db':
        cities = relationship('City', back_populates="state", cascade="all, delete-orphan")

    # For FileStorage
    else:
        @property
        def cities(self):
            """
            Getter attribute cities that returns the list of City instances
            """
            from models import storage
            city_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list