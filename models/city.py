#!/usr/bin/python3
"""This module defines a class City"""
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """This class defines a city by various attributes"""
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')
