#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'))
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities",
                              cascade="all, delete")
    else:
        name = ""
        state_id = ""
