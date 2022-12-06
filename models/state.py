#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", order_by=City.id,
                                backref="state")

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
