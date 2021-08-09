#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            city_dict = models.storage.all(City)
            state_query = self.id
            city_list = []
            for k, v in city_dict.items():
                if v.state_id == self.id:
                    city_list.append(v)
            return city_list
