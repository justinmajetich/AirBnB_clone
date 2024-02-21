#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, VARCHAR

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(VARCHAR(128), nullable=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
