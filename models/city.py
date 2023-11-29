#!/usr/bin/python3
""" Module City for hbnb"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
