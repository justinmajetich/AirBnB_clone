#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",cascade="all, delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
