#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """contains state ID and name"""
    state_id = Column(String(90), ForeignKey('states.id'), nullable=False)
    name = Column(String(200), nullable=False)
    __tablename__ = 'cities'

    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')
