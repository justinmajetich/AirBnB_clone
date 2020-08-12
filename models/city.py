#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id')

    places = relationship("Place", cascade="all, delete", backref="cities")
