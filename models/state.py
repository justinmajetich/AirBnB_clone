#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    from models import dbStorage
    if (dbStorage == 'db'):
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="State")
    else:
        name = ""
