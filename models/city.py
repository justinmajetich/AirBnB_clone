#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """This the city object
    Attributes:
        state_id: State_id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable = False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable = False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")

