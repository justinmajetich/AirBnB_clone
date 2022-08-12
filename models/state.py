#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        cities = relationship("City", backref='State', cascade="delete")
    else:
        @property
        def cities(self):
            "Comment"
            from models import storage
            cities_dict = storage.all('City')
            val_list = []
            for key, value in cities_dict.items():
                if value.state_id == self.id:
                    val_list.append(value)
            return val_list
