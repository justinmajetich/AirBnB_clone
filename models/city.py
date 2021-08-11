#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(128), nullable=False, ForeignKey="states.id")
    places = relationship("Place", backref="cities", cascade="all, delete")
