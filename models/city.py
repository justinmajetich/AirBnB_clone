#!/usr/bin/python3
""" City class """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.placee import Place


class City(BaseModel, Base):
    """ The city clas with
    Attributes:
        state_id: the state id
        name: input name
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    places = relationship(
            "Placee", backref="cities", cascade='all, delete, delete-orphan')
