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
    cities = relationship('cities', backref='state')

    @property
    def cities(self):
        """Getter attribute in case of file storage"""
        from models import storage
        list_city = []
        for key, obj in storage.all(City).items():
            if obj.state_id == self.id:
                list_city.append(obj)
        return list_city
