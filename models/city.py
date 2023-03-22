#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text, Float, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
