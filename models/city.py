#!/usr/bin/python3
""" City Module for HBNB project """
# KASPER edited @ 10/30 11:40pm
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
    ForeignKey
)


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    # places = relationship("Place", backref="cities",
    # foreign_keys='state_id',
    # cascade="all, delete-orphan")
