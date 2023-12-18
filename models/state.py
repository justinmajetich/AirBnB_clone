#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class for storing state info """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # This for DataBase Storage
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="state", cascade="all,
                              delete-orphan")
    else:
        @property
        def cities(self):
            """ Getter attribute for cities (for FileStorage) """
            from models import storage
            city_list = []
            all_cities = storage.all("City")
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
        return city_list
