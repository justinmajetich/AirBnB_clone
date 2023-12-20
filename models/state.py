#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Represents a state
     Attributes:
         name (str): The name of the state
     """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete',
                          back_populates="state")
