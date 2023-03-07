#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
Base = declarative_base()

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name =  Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
