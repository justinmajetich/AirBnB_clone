#!/usr/bin/python3
# KASPER edited 1:45pm 10/28/2023
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    relationship
)

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
