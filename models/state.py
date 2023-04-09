#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

storage_type = os.getenv("HBNB_TYPE_STORAGE","file")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if storage_type == "db":
        cities = relationship("City", backref="state")
    else:
        cities = []
        from models.city import City
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        obj = storage.all(City)
        for val in obj.values():
            if val.state_id == self.id:
                cities.append(val)
        @property
        def cities():
            return self.cities

