#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')

    @property
    def cities(self):
        """cities"""
        from models import storage
        if os.getenv(HBNB_TYPE_STORAGE) != "db":
            cityList = []
            for value in storage.all(City).items():
                for value_2 in storage.all(State).items():
                    if value.state_id == value_2.id:
                        cityList.append(value)
            return cityList
