#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    state_id = Column('state_id', String(60), ForeignKey('states.id'))
    name = Column('name', String(128), nullable=False)
