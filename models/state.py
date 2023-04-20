#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all, delete")
