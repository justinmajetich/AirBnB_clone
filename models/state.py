#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class, inherits from BaseModel and sqlalchemy
    Attributes:
        name: name of state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        """Returns the list of City instances with
        state_id equals to the current State.id
        """
