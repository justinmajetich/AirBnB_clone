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

    cities = relationship("City", backref="state", cascade="delete")
