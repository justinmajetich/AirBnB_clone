#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """ State class which contains __tablename__, name"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
