#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """
    State class
    """
    from models.city import City

    __tablename__ = "states"
    if models.engine_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns cities in State
            """
            cities = []

            for key, value in models.storage.all(City).items():
                if key.split('.')[0] == "City":
                    if self.id == value.state_id and value not in cities:
                        cities.append(value)
            return cities
