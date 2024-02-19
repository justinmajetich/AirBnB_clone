#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    places = relationship(
        "City", cascade="all, delete-orphan", back_populates="state")
