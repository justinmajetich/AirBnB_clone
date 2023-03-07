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
    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == 'db':
        cities = relationship('City',
                              cascade="all, delete-orphan",
                              backref='state'
                              )

    else:
        @property
        def cities(self):
            """ returns list of City instances with matching state ids"""
            from models import storage

            Citylist = []
            for val in storage.all(City).values():
                if val.state_id == self.id:
                    Citylist.append(val)
            return Citylist
