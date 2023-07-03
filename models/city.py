#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    """THE BELOW LINE NEEDS FIX"""
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')

    """relationship between state and city"""
    state_id = Column(int, ForeignKey('states.id'))
    state = relationship("State", backref="cities")
