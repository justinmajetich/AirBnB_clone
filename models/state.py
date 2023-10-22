#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if (os.getenv("HBNB_TYPE_STORAGE") == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref='state')
    else:
        name=""

        @property
        def cities(self):
            """
               returns the list of City instances if
            City.state_id == State.id
            """
            myList = []
            myDict = models.storage.all(City)
            for key, value in myDict.items():
                if (value.state_id == self.id):
                    myList.append(value)
            return (myList)
