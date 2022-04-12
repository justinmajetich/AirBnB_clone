#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="State", cascade='all, delete-orphan')

    else:
        def cities(self):
            """Getter attribute in case of file storage"""
            list_city = []
            for city in range(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
