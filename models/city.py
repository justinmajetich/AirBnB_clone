#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'  # NUEVO REVISAR
    state_id = Column(String(60), ForeignKey(
        'states.id'), nullable=False)  # NUEVO REVISAR
    name = Column(String(128), nullable=False)  # NUEVO REVISAR
    places = relationship("Place", cascade="all, delete", backref="cities")
