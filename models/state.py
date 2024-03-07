#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            """Returns the list of City instances"""
            return_list = list()
            for obj_id, obj in storage.all():
                if not obj_id.startswith("City"):
                    continue
                if getattr(obj, 'state_id', None) == self.id:
                    return_list.append(obj)
            return return_list
