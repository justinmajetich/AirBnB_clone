#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    
"""if storage is db, how do we know?"""
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
"""If storage is file storage"""
    
"""For FileStorage: getter attribute cities that returns the list of 
    City instances with state_id equals to the current State.id => It will 
    be the FileStorage relationship between State and City"""
