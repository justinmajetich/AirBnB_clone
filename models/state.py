#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel, Base):
    """State class repr states"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan",
            primaryjoin='State.id == City.state_id')

    else:
        @property
        def cities(self):
            """ Lists related city objects """
            new_list = []
            current_list = storage.all("City").values()
            for item in current_list:
                if item.state_id == self.id:
                    new_list.append(item)
            return new_list
