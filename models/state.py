#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False, unique=True)
    cities = relationship('City', cascade="all,delete", backref="state")
    # TODO: for FileStorage: getter attribute cities that
    # returns the list of City instances with state_id equals
    # to the current State.id => It will be the FileStorage
    # relationship between State and City
