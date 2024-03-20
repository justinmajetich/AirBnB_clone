#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class State(BaseModel, Base):
    """ State class """
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")
