#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage, storage_type


class State(BaseModel, Base):
    """Defines a ``State`` class"""
    __tablename__ = "states"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """gets all ``City`` instances linked to a state"""
            return [obj for obj in storage.all(City)
                    .values() if obj.state_id == self.id]

    def __repr__(self):
        """Returns a string representation of the ``State`` class"""
        return f"<State: name={self.name}>"
