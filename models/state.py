#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.city import City


class State(BaseModel, Base):
    """State class: mapped to states table"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")

    @property
    def cities(self) -> list:
        """Getter for all City instances with state_id == State.id"""
        city_list = []
        fs = FileStorage()
        all_cities = fs.all(City)

        for key, value in all_cities.items():
            if key == self.id:
                city_list.append({key: value})
        return city_list
