#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
