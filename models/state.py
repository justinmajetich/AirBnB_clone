#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    __tablename__ = 'states'
    """ State class """  
    name =  Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

