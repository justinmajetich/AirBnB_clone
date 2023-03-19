#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(string(60), nullable=False, ForeignKey('states.id'))
    name = Column(string(128), nullable=False)

    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
