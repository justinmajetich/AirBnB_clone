#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """Class to declare the State model or states database table
    """
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", back_populates="state", cascade="delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """FileStorage Getter that returns

                Returns:
                    List of Cities with state_id of current instance id
            """
            from models.__init__ import storage
            from models.city import City

            data = storage.all(City)
            filtered = []
            for k, v in data.items():
                if k.split('.')[0] == "City" and self.id == v.state_id:
                    filtered.append(v)

            return filtered
        