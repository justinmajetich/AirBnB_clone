#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = Column(str(60), Foreignkey('state.id'), nullable=False)
    name = Column(str(128), nullable=False)
    __tablename__ = cities
