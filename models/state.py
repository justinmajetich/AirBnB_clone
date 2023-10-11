#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

        if getenv("HBNB_TYPE_STORAGE") != 'db':
            @property
            def cities(self):
                """getter for cities"""
                city_list = []
                for city in models.storage.all('City').values():
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list
