#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.state import State


class City(BaseModel):
    """
    City class that inherit from BaseModel
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
