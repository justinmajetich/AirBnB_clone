#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter attribute in case of file storage"""
        from models import storage
        list_city = []
        for key, obje in storage.all(City).item():
            if obje.state_id == self.id:
                list_city.append(obje)
        return list_city
