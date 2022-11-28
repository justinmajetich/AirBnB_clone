#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            obj_list = []
            for i in list(storage.all(City).values()):
                if i.state_id == self.id:
                    obj_list.append(i)
            return obj_list
