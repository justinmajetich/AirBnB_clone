#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
