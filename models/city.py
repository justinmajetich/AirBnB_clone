#!/usr/bin/python3
""" City Module for AirBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')
