#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

st = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if st == "db":
        name = Column(String(128), nullable=False)

        cities = relationship("City", back_populates="state")
    else:
        name = ""
        @property
        def cities(self):
            """getter method for the filestorage"""

            from models import storage
            obj = storage.all()
            lst = list(obj)
            new =[]

            for i in lst:
                if "City" in i:
                    new.append(City(obj[i]))
