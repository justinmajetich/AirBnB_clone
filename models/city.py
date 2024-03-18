#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class """
    __tablename__ = 'cities'

    state_id = ""
    name = ""

    places = relationship("Place", cascade="all, delete",
                          backref="city", passive_deletes=True)
