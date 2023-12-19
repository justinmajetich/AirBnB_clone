#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if models.storage_type == 'db':
        cities = relationship('City', cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """Getter attribute for cities in FileStorage"""

            city_list []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
