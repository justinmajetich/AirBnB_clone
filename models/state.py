#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.engine.file_storage import FileStorage as F
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """get the list of City instances of the same state"""
        for city in F.all('City').values():
            city_list = []
            if city.state_id == self.State.id:
                city_list.append(city)

        return city_list
