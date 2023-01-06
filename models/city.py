#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseMode, Base
from sqlalchemy improt Column, Integer, String
from sqlalchemy import ForeignKey
from sglalchemy.orm import relationship
from models.place import Place


class City(BaseModel):
    """ The city class, contains state ID and name
    state_id = ""
    name = ""
    """
    __tablename__ = "citites"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    places = relationship("Places", cascade='all, delete, delete-orphan', backref="cities")
