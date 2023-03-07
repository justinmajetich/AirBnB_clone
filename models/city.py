#!/usr/bin/python3
"""
Defines the City class.
"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city for a MySQL database."""

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)