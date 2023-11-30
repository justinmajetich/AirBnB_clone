#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Init for inherited BaseModel"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def cities(self):
            """getter for cities taht return
            a list of city instance equal to
            current state id
            """
            list_city = []
            all_inst_c = models.storage.all(City)
            for value in all_inst_c.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city
