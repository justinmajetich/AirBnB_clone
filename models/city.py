#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String ForeignKey
from models.__init__  import storage_type

Base = declarative_base

class City(BaseModel, Base):
    """ 
    The city class, contains state ID and name 
    """
    if storage_type = 'db':
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey=('state_id'),
                          nullable=False)
    else:
        state_id = ""
        name = ""
