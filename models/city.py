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

    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')
