#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String
import os
import models

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    cities  = relationship('City', cascade='all, delete-orphan',
            backref='state')
    name = column(string(128), nullabe=False)
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self)
        """
        returns a list of the City instance with their
        specific state_id
        """
        new_list = []
        city_inst = models.storage.all(models.classes['city']).value()
        for k in city_inst:
            new_list.append(k)
        return new_list
