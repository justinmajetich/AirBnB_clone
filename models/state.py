#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        @property
        def cities(self):
            """Returns the list of Cities with state_id equal to current State.id"""
            from models import storage
            l = []
            for v in storage.all().values():
                if v.state_id == self.id:
                    l.append(v)
            return l
