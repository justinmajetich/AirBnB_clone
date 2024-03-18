#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              passive_deletes=True, backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """cities property getter"""
        city_lst = []
        for key, val in models.storage.all().items():
            try:
                if val.state_id == self.id:
                    city_lst.append(val)
            except AttributeError:
                pass
        return city_lst
