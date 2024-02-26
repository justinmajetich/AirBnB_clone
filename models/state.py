#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = Column(str(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship("City", cascade="all, delete", backref="state")

def cities(self):
    """attribute for getter for FileStorage"""
    return [city for city in self.cities if city.state_id == self.id]