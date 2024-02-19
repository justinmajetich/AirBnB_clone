#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    places = relationship(
        "Place", cascade="all, delete-orphan", back_populates="city")
