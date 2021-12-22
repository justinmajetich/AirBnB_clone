#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Coulmn, String

class State(BaseModel, Base):
    """ State class
    inherits from BaseModel and Base
    (respects the order)
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
