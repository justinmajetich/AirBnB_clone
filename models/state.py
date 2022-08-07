#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey, Column
from models.base_model import Base
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ returns the list of City instances
            with the appropriate state_id
            """
            list_city = []
            c = list(models.storage.all(City).values)
            for city in c:
                if city.state_id == self.id:
                    list_city.append(city)

            return list_city
