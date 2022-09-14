#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import Base
from models.state import state
from sqlalchemy import Column, String, Integer

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    __tablename__  = 'cities'
    name = column(string(128), nullable=False)
    state_id = column(string(60), ForeignKey('states.id'), nullabe=False)
    places = relationship('Place', cascade="all, delete", backref='cities')
