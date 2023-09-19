#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class State(BaseModel, Base):
    """ State class redefined to use sqlalchemy """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city_id, city_obj in storage.all(City).items():
                if city_obj.state_id == self.id:
                    city_list.append(city_obj)
            return city_list
