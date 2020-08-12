#!/usr/bin/python3
""" 0x02. AirBnB clone - MySQL, task 6. DBStorage - States and Cities """
from sqlalchemy import Column, String
from sqlalchemy.schema import ForeignKey
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """Defines attributes for `City` as it inherits from `BaseModel`,
    and ORM properties in relation to table `cities`.
    
    Attributes:
        name (Column): name of state, string of max 128 chars 
        state_id (Column): string of max 60 chars, foreign key to `states.id` 
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
