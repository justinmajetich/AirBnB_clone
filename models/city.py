#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            "Initiats the city attributes"
            self.name = ""
            self.state_id = ""
    else:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False,
                          ondelete="CASCADE")
