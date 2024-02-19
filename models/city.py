#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel):
    """ The city class, contains state ID and name """
    
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    place = relationship("Place", backref="cities", cascade="all, delete-orphan")
