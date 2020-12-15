#!/usr/bin/python3
""" City Module for HBNB project """


from models.base_model import BaseModel, Base
from models.state import state
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __Tablename__ = "cities"
    state_id = Column(String(60), nullable=False, Foreingkey=(state_id))
    name = Column(String(128), nullable=False)
