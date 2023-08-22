""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # relationship to get all cities of this state saved in db
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")

    elif getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """Getter for cities of this state saved in FileStorage"""
            cities = []
            # filter for all cities that are in FileStorage
            for city in models.storage.all(City).values():
                # grab only cities that have this as their state
                if city.state_id == self.id:
                    cities.append(city)
            return cities