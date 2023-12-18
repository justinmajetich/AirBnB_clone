#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
     """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')


    def to_dict(self):
        """Converts instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
