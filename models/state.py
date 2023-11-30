#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os ## double check circular import

class State(BaseModel, Base):

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""
