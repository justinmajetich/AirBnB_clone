#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel):
    """ The city class, contains state ID and namegit add .
    """
__tablename__ = "cities"
# Represents a column containing a string (128 characters)
name = Column(String(128), nullable=False)
# Represents a column containing a string (60 characters)
# It is a foreign key to states.id
state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    
