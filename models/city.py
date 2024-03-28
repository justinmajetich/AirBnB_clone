#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """Class to declare the cities database table
    """
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities",
                              cascade="delete, delete-orphan")
    else:
        name = ""
        state_id = ""
        