#!/usr/bin/python3
# KASPER edited @ 10/30 11:40pm
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
)


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan",
                          primaryjoin='State.id == City.state_id')
