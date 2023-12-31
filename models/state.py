#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

        cities = relationship(
            "City", cascade="all, delete, delete-orphan",
            back_populates="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter method for the filestorage"""

            from models import storage
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
