#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel, Base): # +T6: Base
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # state_id = "" -T6
    state_id = Column(String(60), nullable=False, ForeignKey('states.id')) # +T6
    # name = "" # -T6
    name = Column(String(128), nullable=False) # +T6
