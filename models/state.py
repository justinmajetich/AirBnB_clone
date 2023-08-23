#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            back_populates="state", cascade="all, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """ Returns City instances with state_id """
            from models import storage
            city_instances = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_instances.append(city)
            return city_instances
