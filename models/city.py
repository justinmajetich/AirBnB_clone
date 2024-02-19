#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship(
        "State", back_populates="city")
    places = relationship(
        "Place", cascade="all, delete-orphan", back_populates="city")
