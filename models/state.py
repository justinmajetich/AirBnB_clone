#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='delete')
    else:
        @property
        def cities(self):
            """cities getter"""
            from models import storage
            cities_list = []
            for key, value in storage.all().items:
                if 'City' in key and value.state_id == self.id:
                    cities_list.append(value)
            return cities_list
