#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """State class repr states"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan",
        primaryjoin='State.id == City.state_id')

    @property
    def cities(self):
        """ Lists related city objects """
        new_list = []
        current_list = storage.all()
        for item in current_list:
            object = current_list[item].to_dict()
            if object["__class__"] == "City" and object["state_id"] == self.id:
                new_list.append(current_list[item])
        return new_list
