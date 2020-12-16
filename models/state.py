#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)  # NUEVO REVISAR
    cities = relationship("City", cascade="all, delete", backref="state")

    @property  # NUEVO REVISAR
    def cities(self):
        from models.__init__ import storage
        city_list = []
        for value in storage.all(City).values():
            if self.id == value[state_id]:
                city_list += value
        return city_list
