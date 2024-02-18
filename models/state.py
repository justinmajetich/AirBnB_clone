#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    # name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        from models import storage
        city_dict = storage.all("City")
        state_cities = []
        for value in city_dict.values():
            if value.state_id == self.id:
                state_cities.append(value)
        return state_cities
