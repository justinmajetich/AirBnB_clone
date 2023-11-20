#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNH_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all("City")
            temp = []
            for city in cities:
                if all_cities[city].state_id == self.id:
                    temp.append(all_cities[city])

            return temp
