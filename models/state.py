#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from . import storage
import uuid

class State(BaseModel, Base):
    """ State class """
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        State.name = kwargs.get('name', State.name)
        super().__init__(*args, **kwargs)
