#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances"""
        new_list = []
        for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return new_list


