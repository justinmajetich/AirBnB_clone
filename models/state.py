#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref='state')

    @property
    def cities(self):
        """Returns all cities of a specific state"""
        dictionary = models.storage.all()
        _list = []
        for key in dictionary:
            key = shlex.split(key.replace('.', ' '))
            if key[0] == 'City':
                _list.append(dictionary[key])
        return [item for item in _list if item.state_id == self.id]
