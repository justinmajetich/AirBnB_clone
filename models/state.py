#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Relationship
from models import storage_type
from sqlalchemy import Column, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = Relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

    @property
    def cities(self):
        """
        Returns the list of City instances with state_id
        equals to the current State.id
        """
        from models import storage
        all_cities = storage.all(City)
        my_city = []
        city_obj = list(all_cities.values())
        for obj in city_obj:
            if obj.state_id == self.id:
                my_city.append(obj)
        return my_city
