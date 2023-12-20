#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
from models.city import City


Base = declarative_base()

strg = os.getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if strg == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute for cities in FileStorage"""

            city_list =  []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
