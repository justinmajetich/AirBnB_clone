#!/usr/bin/python3
""" module for class State """
import models
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ class for City

        Attributs
        ===================

            name : name of City
                String, not null
            state_id: ForeignKey (class State), not null string
            place: relationship with class Place
    """
    __tablename__ = 'cities'

    # if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    name = Column(
        String(128),
        nullable=False)
    state_id = Column(
        String(60),
        ForeignKey('states.id'),
        nullable=False)
    places = relationship(
        'Place', backref='cities', cascade='delete')
    # else:
    #     name = ""
    #     state_id = ""
