#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

st = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    
    if st == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)


        state = relationship("State", back_populates="cities")


        places = relationship("Place", cascade="all,delete, delete-orphan, merge, save-update", back_populates="cities")

    else:
        name = ""
        state_id = ""
