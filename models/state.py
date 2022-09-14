#!/usr/bin/python3
'''
    Implementation of the State class
'''
import os
import models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan',
                          backref='state')

    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """
            Returns list of City instances with specific state id
            """
            res = []
            city_inst = models.storage.all(models.classes['City']).values()
            for k in city_inst:
                if k.state_id == self.id:
                    res.append(k)
            return res
