#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")

    @property
    def cities(self):
        """Getter Attribute of cities returns the list of city instances"""
        from models import storage

        new_dict, state_instance = storage.all(), []
        for keys, values in new_dict.items():
            if key.split(".")[0] == "City":
                if values["id"] == self.id:
                    state_instance.append(values)
