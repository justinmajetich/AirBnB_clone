#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete",
        backref="state",
    )

    @property
    def cities(self):
        from models import storage
        from models.city import City
        dictionary = storage.all(City)
        list_of_city = []
        for v in dictionary.values():
            if self.id == v.state_id:
                list_of_city.append(v)
        return list_of_city
