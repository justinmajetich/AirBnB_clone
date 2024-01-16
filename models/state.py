#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
from sqlalchemy import String, Integer, Table
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
