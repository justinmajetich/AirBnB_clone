#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    # fmt: off
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False)
    # fmt: on

    # Relationships
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # fmt: off
        places = relationship(
            'Place', backref='cities', cascade='all, delete')
        # fmt: on
