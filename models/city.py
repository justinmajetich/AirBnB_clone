#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
import models
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """city details"""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
