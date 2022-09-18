#!/usr/bin/python3
""" State Module for HBNB project """

from tempfile import gettempprefix
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Getter attribute for FileStorage class"""
        cities = storage.all("City")
        cty = []
        for i in cities:
            if cities[i] == self.id:
                cty.append(cities[i])
        return cty
