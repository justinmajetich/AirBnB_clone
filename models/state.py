#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.engine.file_storage import Base


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Initialize instance of state creation """
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
