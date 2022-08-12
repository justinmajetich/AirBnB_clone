#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            "Comment"
            import models
            val_list = []
            city_dict = models.storage.all('City')
            for key, value in city_dict.items():
                if self.id == value.state_id:
                    val_list.append(value)
            return val_list
    else:
        cities = relationship("City", backref="State", cascade="delete")
