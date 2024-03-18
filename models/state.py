#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            from models import storage
            city_list = storage.all(City)
            return [city for city in city_list.values()
                    if city.state_id == self.id]
