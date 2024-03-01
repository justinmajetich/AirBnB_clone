#!/usr/bin/python3
"""City Module for HBNB project"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel


class City(BaseModel):
    """The city class, contains state ID and name"""
    state_id = Column(Integer, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
