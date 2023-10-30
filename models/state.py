#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # For DBStorage
    if models.storage_type == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    # For FileStorage
    if models.storage_type == "file":
        @property
        def cities(self):
            city_list = []
            for city_id, city in models.storage.all("City").items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
