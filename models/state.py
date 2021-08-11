#!/usr/bin/python3
""" State Module for HBNB project """

from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all")

    else:
        def cities(self):
            """ Return the list of City instances with state_id """
            from models import storage
            city_list = []

            for ct in storage.all(City).values():
                if ct.state_id == self.id:
                    city_list.append(ct)

            return city_list
