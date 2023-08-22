#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, Integer, Nullable, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = column(String(60), ForeignKey('states.id'), Nullable=False)
        name = column(String(128), Nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        state_id = ""
