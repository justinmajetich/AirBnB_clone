#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel #, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#temp comment out
#class City(BaseModel, Base):
class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', String(60), ForeignKey('states.id'), nullable=False)

    state = relationship('State', back_populates='cities')
    places = relationship('Place', back_populates='city', cascade='all, delete-orphan')
