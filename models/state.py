#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = states
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_ref='states')


    @property
    def cities(self):
        """cities"""
        for city in storage.all().items():
            if 

