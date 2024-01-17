#!/usr/bin/python3
""" City class """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import state


class City(BaseModel, Base):
    """ The city clas with 
    Attributes:
        state_id: the state id
        name: input name
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    state = relationship("State", back_populates="cities")
