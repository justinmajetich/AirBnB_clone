#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlachemy import Column, String, Foreignkey
from sqlalchemy.orm import relastionship
from model.base_model import BaseModel, Base

class State(BaseModel):
    """ State class """
    __tablename__ = 'state'
    name = Column(String(128), nullable=False)
    cities = relationship('city', backref='state', cascade='all, delete-orphan',
            passive_deletes=True)
