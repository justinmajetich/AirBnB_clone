#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """Name of table in database to link to"""
    __tablename__ = "states"

    """This class defines a user by name & state_id attributes"""
    name = Column(String(128), nullable=False)

    """Check if env variable is db(sql), if so create rel w/ state"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', cascade='all, delete-orphan', backref='state')
        """If env variable is not db(sql), its FileStorage"""
    else:
        @property
        def cities(self):
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
