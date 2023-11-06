#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import uuid


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True,
                default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """"""
            from models import storage
            c_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    c_list.append(city)
            return (c_list)

