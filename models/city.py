#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('Place',
                          cascade='all, delete-orphan', backref='city')
