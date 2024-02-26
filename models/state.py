#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column


class State(BaseModel, Base):
    """ State class """
    name = Column(str(128), nullable=False)
    __tablename__ = 'states'


