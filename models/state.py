#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import backref, relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """getter for cities relationship for FileStorage"""
        City_Class = BaseModel.all_classes('City')
        result = models.storage.all(City_Class)
        selected_city = [v for k, v in result.items()
                         if v.state_id == self.id]
        return selected_city

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref=backref('state'))
