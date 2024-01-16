#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
from sqlalchemy impot Column, Integer, String, ForeignKey
from sqlachemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(128),ForiegnKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
