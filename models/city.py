#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel):
    """ The city class, contains state ID and name """
    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='delete')
    else:
        state_id = ""
        name = ""
