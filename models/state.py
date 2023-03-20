#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import storage
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE", "Storage type not set")

if storage_type == 'db':
    class State(BaseModel, Base):
        """Defines a ``State`` class"""
        if storage_type == 'db':
            __tablename__ = "states"
            name = Column(String(128), nullable=False)
            cities = relationship("City", backref="state",
                                  cascade="all, delete, delete-orphan")
        else:
            name = ""

            @property
            def cities(self):
                """gets all ``City`` instances linked to a state"""
                return [obj for key, obj in storage.all('City')
                        .items() if obj.state_id == self.id]

        def __repr__(self):
            """Returns a string representation of the ``State`` class"""
            return f"<State: name={self.name}>"
