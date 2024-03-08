#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .city import City
import os
from .base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column('name', String(128), nullable=False)
    
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            return [city for city in City.query.filter_by(state_id=self.id).all()]
