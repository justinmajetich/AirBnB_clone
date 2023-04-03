#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="states")
