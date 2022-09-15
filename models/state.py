#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Represents a State for the MySQL database 
    Inherits from BaseModel and Base(SqlAlchemy)

    Attributes:
      __tablename__(str): name of the table in MySQL
      name(Sqlalchemy String): name of a State
      cities (sqlalchemy relationship): The State-City relationship.
    """
    if models.storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        def __init__(self, name = ""):
            """ if storage_type is not db initialize parameters """
            self.name = name
            super().__init__()

        @property
        def cities(self):
            """Get a list of all related City objects"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

