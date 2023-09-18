#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
