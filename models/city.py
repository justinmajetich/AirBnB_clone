#!/usr/bin/python3
"""
City Module for HBNB project
"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
import uuid

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    id = Column(String(60), nullable=False, primary_key=True, default=uuid.uuid4().hex)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
