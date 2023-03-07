#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """Name of table in database to link to"""
    __tablename__ = "cities"

    """This class defines a user by name & state_id attributes"""
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    """Check if env variable is db(sql), if so create rel w/ place"""
    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == 'db':
        places = relationship('Place',
                              cascade="all, delete, delete-orphan",
                              backref='cities')
