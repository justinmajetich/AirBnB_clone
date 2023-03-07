#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
Base = declarative_base 


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ ='cities'
    state_id = Column(String(128), nullable=False)
    name =  Column(String(128), nullable=False)
states = relationship('State', backref='cities', cascade='delete')