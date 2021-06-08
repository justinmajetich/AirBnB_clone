#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """getter attribute cities for FileStorage"""
        from models import storage
        city_inst_list = []
        for value_city in storage.all(City).values():
            if value_city.state_id == self.id:
                city_inst_list.append(value_city)
        return city_inst_list
