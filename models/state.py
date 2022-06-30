#!/usr/bin/python3
"""State Module"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """info for fileStorage"""
            city_list = []
            for el in models.storage.all(City).values():
                if el.state_id == self.id:
                    city_list.append(el)
            return city_list
