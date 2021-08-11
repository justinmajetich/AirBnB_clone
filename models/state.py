#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete",
                              backref="cities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes class"""
        super().__init__(*args, **kwargs)
