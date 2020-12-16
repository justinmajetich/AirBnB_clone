#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False) #NUEVO REVISAR
    cities = relationship("City", cascade="all, delete", backref="state") #NEW REVISAR

    @property #NUEVO REVISAR
    def cities(self)
        city_list = []
        for value in storage.all(City).values():
            if self.id == value[state_id]:
                city_list += value
        return city_list
