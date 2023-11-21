#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from model.state import State
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref='cities')
