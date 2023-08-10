#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
                                "City",
                                backref='state',
                                cascade="all, delete-orphan"
                                )

else:
    class State(BaseModel):
        """ State class """
        name = ""
