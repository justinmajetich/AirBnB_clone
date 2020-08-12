#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os


class City(BaseModel, Base):
    """ City class, contains state ID and name """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")

    else:
        name = ""
        state_id = ""
