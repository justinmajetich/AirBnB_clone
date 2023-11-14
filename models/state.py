#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class repr states"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_list = relationship(
            "City", backref="state", cascade="all, delete-orphan",
            primaryjoin='State.id == City.state_id')

    else:
        @property
        def cities(self):
            """ Lists related city objects """
            return self.city_list
